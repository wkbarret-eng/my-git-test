## 刪除原有的 Docker 映像檔：
```bash=
$ sudo docker images
[sudo] password for ubuntu: 
REPOSITORY        TAG       IMAGE ID       CREATED             SIZE
docker-demo-app   latest    8d8665bf394e   About an hour ago   1.03GB
python            latest    ae29c48b7429   4 weeks ago         1.02GB
```

## 刪除映像檔
```bash=
$ sudo docker rmi 8d8665bf394e
Untagged: docker-demo-app:latest
Deleted: sha256:8d8665bf394e979aa43078395e651f9c6055957900c13530a5984cdf4d995aec
Deleted: sha256:b4862502546406e8985e7969336c643288ce9a77a078cda282f199ea2a2f8a89
Deleted: sha256:a8b755a7e79481831ce2356450ca5d5ffe7ed4c2ccf3ab4df674914c304b771a
Deleted: sha256:fbcae5dcfe78196f9716cdacdffafbd6abd7d826f16af5eb57dfd01fb4b2a184
Deleted: sha256:ddf785c83ab29db68fca6d396d542619049082db6fbc0b453837001913ccd47f
Deleted: sha256:abbcd5f3bf670e8b1538c8851d1361aac24fc162ca6873813653de30a12b5470
Deleted: sha256:824cd39aca64b9129777fdb58baf1fbe29f1a1bf1d64fbf551b88656af5cf424
Deleted: sha256:8774a17a01b0b175ba2dd5c7aad58a704bd7a6552f73d072267752a71f5233fa
Deleted: sha256:f37ea8c5892d923676f0283bdc0e3a4503d6288c7efdf95377af4e8afda28aad
```



## 編譯 Docker image
```bash=
$ sudo docker build . -t docker-demo-app
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  6.144kB
Step 1/9 : FROM python:latest
 ---> ae29c48b7429
Step 2/9 : LABEL version="1.0"       Copyright="2024"       owner="yillkid"
 ---> Running in 85174db60bc3
Removing intermediate container 85174db60bc3
 ---> a354231c1640
Step 3/9 : ENV SERVICE_PORT=5001
 ---> Running in 6dbae8a8dab0
Removing intermediate container 6dbae8a8dab0
 ---> 04a0381a594b
Step 4/9 : WORKDIR /app
 ---> Running in defd2d27f65c
Removing intermediate container defd2d27f65c
 ---> 3b3234b53594
Step 5/9 : ADD https://raw.githubusercontent.com/4-learn/flask-hello/main/server.py /app/server.py
Downloading     237B
 ---> a2d1c986084b
Step 6/9 : ADD https://raw.githubusercontent.com/4-learn/flask-hello/main/requirements.txt /app/requirements.txt
Downloading       6B
 ---> 335dff4c1357
Step 7/9 : RUN pip install -r /app/requirements.txt
 ---> Running in 11755bb55b15
Collecting flask (from -r /app/requirements.txt (line 1))
  Downloading flask-3.0.2-py3-none-any.whl.metadata (3.6 kB)
Collecting Werkzeug>=3.0.0 (from flask->-r /app/requirements.txt (line 1))
  Downloading werkzeug-3.0.1-py3-none-any.whl.metadata (4.1 kB)
Collecting Jinja2>=3.1.2 (from flask->-r /app/requirements.txt (line 1))
  Downloading Jinja2-3.1.3-py3-none-any.whl.metadata (3.3 kB)
Collecting itsdangerous>=2.1.2 (from flask->-r /app/requirements.txt (line 1))
  Downloading itsdangerous-2.1.2-py3-none-any.whl.metadata (2.9 kB)
Collecting click>=8.1.3 (from flask->-r /app/requirements.txt (line 1))
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting blinker>=1.6.2 (from flask->-r /app/requirements.txt (line 1))
  Downloading blinker-1.7.0-py3-none-any.whl.metadata (1.9 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask->-r /app/requirements.txt (line 1))
  Downloading MarkupSafe-2.1.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)
Downloading flask-3.0.2-py3-none-any.whl (101 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.3/101.3 kB 781.0 kB/s eta 0:00:00
Downloading blinker-1.7.0-py3-none-any.whl (13 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 1.6 MB/s eta 0:00:00
Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Downloading Jinja2-3.1.3-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.2/133.2 kB 2.1 MB/s eta 0:00:00
Downloading werkzeug-3.0.1-py3-none-any.whl (226 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 226.7/226.7 kB 1.9 MB/s eta 0:00:00
Downloading MarkupSafe-2.1.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (28 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
Successfully installed Jinja2-3.1.3 MarkupSafe-2.1.5 Werkzeug-3.0.1 blinker-1.7.0 click-8.1.7 flask-3.0.2 itsdangerous-2.1.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
Removing intermediate container 11755bb55b15
 ---> da0a602fc163
Step 8/9 : EXPOSE 5001
 ---> Running in 577bad3e3802
Removing intermediate container 577bad3e3802
 ---> 0123da4b9790
Step 9/9 : CMD ["python3", "server.py"]
 ---> Running in 062cd52eadbd
Removing intermediate container 062cd52eadbd
 ---> 70a9d85b14e0
Successfully built 70a9d85b14e0
Successfully tagged docker-demo-app:latest
```

## 檢查映像檔
```bash=
$ sudo docker images
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
docker-demo-app   latest    70a9d85b14e0   51 seconds ago   1.03GB
python            latest    ae29c48b7429   4 weeks ago      1.02GB
```

## 運行容器
```bash=
s sudo docker run -ti 70a9d85b14e0$ 

 * Serving Flask app 'server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://172.17.0.2:5001
Press CTRL+C to quit
```
