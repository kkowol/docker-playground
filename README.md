# docker-playground
build the container:
```
docker build -t semseg:latest .
```

start the container in the current directory:
```
docker run -v "$(pwd)/prediction:/home/semseg/prediction" semseg
```
