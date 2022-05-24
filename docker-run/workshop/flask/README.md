# Docker Image exmaple

## Build
sudo docker build . -t docker-flask

## Run
sudo docker run -d --restart=always --net=bridge -p 3001:3001 -it docker-flask
