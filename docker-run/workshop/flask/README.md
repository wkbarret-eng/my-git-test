# Docker Image exmaple

## Build
docker build . -t docker-flask

## Run
docker run -d --restart=always --net=bridge -p 3001:5001 -it docker-flask
