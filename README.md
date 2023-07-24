# docker-playground

## Prerequisites
you need to install docker and the nvidia-container-toolkit for using the GPUs.\
follow these instructions: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

## build container
1. create a new folder and copy the Dockerfile into it

2. build the container inside the folder:
```
docker build -t semseg:latest .
```

## start container
1. create a folder with the name ```images``` and copy all the images that you want to infer
2. start the container, which creates the prediction masks into the folder ```prediction```
3. start the container in the current directory with GPU acceleration:
```
docker run -v "$(pwd)/images:/home/semseg/images" -v "$(pwd)/prediction:/home/semseg/prediction" --gpus all semseg
```
