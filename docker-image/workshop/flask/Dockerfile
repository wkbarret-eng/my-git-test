FROM python:latest

LABEL version = "1.0" Copyright = "2024" owner = "yillkid"

EXPOSE 5001 

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD python3 server.py
