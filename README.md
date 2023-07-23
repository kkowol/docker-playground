# docker-playground
1. create a new folder and copy the Dockerfile into it

2. build the container inside the folder:
```
docker build -t semseg:latest .
```

3. start the container in the current directory:
```
docker run -v "$(pwd)/prediction:/home/semseg/prediction" semseg
```
## how to infer new images
1. create a folder with the name ```images``` and copy all the images that you want to infer
2. start the container, which creates the prediction masks into the folder ```prediction```
