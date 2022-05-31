# Docker Image exmaple

## Build
sudo docker build . -t docker-flask

## Run
sudo docker run -d --restart=always --net=bridge -p 3001:5001 -it docker-flask
