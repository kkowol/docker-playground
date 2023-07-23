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
