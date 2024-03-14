## 先確定有 Flask Docker image
```bash=
$ docker images | grep flask
docker-flask   latest    8b684bcd6760   5 minutes ago   1.03GB
```

## 銷售部門的 Docker Container 配置
```bash=
$ docker run -d --name flask-sales --network="host" -p 5001:5001 docker-flask
```
 
## 群募部門的 Docker Container 配置
```bash=
$ docker run -d --name flask-crowdfunding -p 5002:5001 docker-flask
```

## 檢查
```bash=
$ docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
docker-flask   latest    8b684bcd6760   11 minutes ago   1.03GB
python         latest    ae29c48b7429   5 weeks ago      1.02GB
$ docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
f1615227e0b1   docker-flask   "/bin/sh -c 'python3…"   16 seconds ago   Up 16 seconds   0.0.0.0:5002->5001/tcp, :::5002->5001/tcp   flask-crowdfunding
19f8066fd8f7   docker-flask   "/bin/sh -c 'python3…"   39 seconds ago   Up 39 seconds                                               flask-sales
$ sudo netstat -ntlp | grep 500
[sudo] password for ubuntu: 
tcp        0      0 0.0.0.0:5001            0.0.0.0:*               LISTEN      13773/python3       
tcp        0      0 0.0.0.0:5002            0.0.0.0:*               LISTEN      13800/docker-proxy  
tcp6       0      0 :::5002                 :::*                    LISTEN      13807/docker-proxy   
```
