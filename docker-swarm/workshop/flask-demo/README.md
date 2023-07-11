# Workshop - Swarm-flask

## Swarm 建立 ( 有做過就不用做了 )
#### 1. Manager : swarm init
- command
```bash=
sudo docker swarm init
```
- output
```bash=
$ sudo docker swarm init
Swarm initialized: current node (m7b4v08ps23yz3d9kfxvivpec) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-1gxwztivnqzyips2dt6i9f3hmpk51hiehbqzbl3ptrlsfiv160-5d4btswrdsn2zwz4ab94cpkho 192.168.224.5:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.

```

#### 2. Worker : join
```bash=
$ docker swarm join --token SWMTKN-1-1gxwztivnqzyips2dt6i9f3hmpk51hiehbqzbl3ptrlsfiv160-5d4btswrdsn2zwz4ab94cpkho 192.168.224.5:2377
This node joined a swarm as a worker.
```

#### 3. Docker swarm node ls ( n manager)
```bash=
 sudo docker node ls
ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
m7b4v08ps23yz3d9kfxvivpec *   devops     Ready     Active         Leader           20.10.21
69p7eacn7vzu7k5r00m8v7l5l     yillkid    Ready     Active                          20.10.21
```


## 佈署 Swarm
#### 1. Login
```bash=
$ sudo docker login 
```

#### 2. 編譯 Docker image
- command
```bash=
$ sudo docker build -t yillkid/flask-swarm:latest .
```
- output
```bash=
... skip ...
Successfully built e4bbe11f4de9
Successfully tagged yillkid/flask-swarm:latest
```

#### 3. Push to Docker hub
- command
```bash=
$ sudo docker push yillkid/flask-swarm:latest
```
- output
```bash=
$ sudo docker push yillkid/flask-swarm:latest
The push refers to repository [docker.io/yillkid/flask-swarm]
8a9ce5932931: Pushed 
b10bbbd8f247: Pushed 
a9a1dfa0b8c5: Mounted from yillkid/flask-demo-swarm 
83026ecbbeb7: Mounted from yillkid/flask-demo-swarm 
e49c94d01395: Mounted from yillkid/flask-demo-swarm 
f1acaab90728: Mounted from yillkid/flask-demo-swarm 
28218ecd8008: Mounted from yillkid/flask-demo-swarm 
2f66f3254105: Mounted from yillkid/flask-demo-swarm 
a72216901005: Mounted from yillkid/flask-demo-swarm 
61581d479298: Mounted from yillkid/flask-demo-swarm 
latest: digest: sha256:1e194bb1ea6f472e6facefc30ac8d5019266051580d7d453bdf91a3d48e43cf8 size: 2426
```

#### 4. swarm deploy
- command
```bash=
$ sudo docker stack deploy --compose-file flask-app.yml apps --with-registry-auth
```
- output
```bash=
$ sudo docker stack deploy --compose-file flask-app.yml apps --with-registry-auth
Creating network apps_appnet
Creating service apps_flask
```

## 預期輸出

#### manager:
```bash=
$ curl -XGET http://192.168.224.5:8080
Container Hostname: aa1274b3bc4b , UUID: 25fdc7e0-cff4-4030-a0b9-5cf039a3bf1d
```

#### worker:
```bash=
$ curl -XGET http://192.168.224.4:8080
Container Hostname: 23dffca9afb7 , UUID: 62453314-df15-4bea-a555-6caac168a800
```
