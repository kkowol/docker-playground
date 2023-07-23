import os
import pickle as pkl
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from torchvision.transforms import Compose, Normalize, ToTensor
from torch.utils.data import DataLoader
from PIL import Image

from src.model.deepv3 import DeepWV3Plus
import src.datasets.cityscapes as cs


def prediction(net, image, dvc):
    image = image.to(dvc)
    with torch.no_grad():
        out = net(image)
    out = out.data.cpu()
    out = F.softmax(out, 1)
    return out.numpy()

def from_path_to_input(path):
    img = Image.open(path)
    trans = Compose([ToTensor(), Normalize(cs.mean, cs.std)])
    img = trans(img)
    img = img.unsqueeze(0)
    return img

def load_network(num_classes=19, ckpt_path='./cityscapes_best.pth', dvc = torch.device("cuda")):
    net = nn.DataParallel(
        DeepWV3Plus(num_classes))
    net.load_state_dict(torch.load(ckpt_path, map_location= dvc)['state_dict'], strict=False)
    net = net.to(dvc)
    net.eval()
    return net

def color_image(arr):
    predc = [cs.trainid_to_color[arr[p, q]] for p in range(arr.shape[0]) for q in range(arr.shape[1])]
    predc = np.asarray(predc).reshape(arr.shape + (3,))
    return predc


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    net = load_network(19, './cityscapes_best.pth', device)
    print("Network loaded")

    if not os.path.exists("prediction"):
        os.mkdir("prediction")

    for im in os.listdir('./images'):
        img = os.path.join('./images', im)
        inp = from_path_to_input(img)
        print("Image loaded")
        softmax = prediction(net, inp, device)
        softmax = np.squeeze(softmax)
        print("Softmax predicted")
        pred = np.argmax(softmax, axis=0)
        pred = np.squeeze(pred)
        pred_c = color_image(pred)
        Image.fromarray(pred_c.astype('uint8')).save(os.path.join('./prediction', im))
        
if __name__ == "__main__":
    main()
