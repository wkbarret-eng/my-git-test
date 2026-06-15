# 使用 python 官方映像檔的最新版作為基礎
FROM python:latest

# 設定標籤資訊
LABEL version="1.0" \
      Copyright="2024" \
      owner="yillkid"

# 設定環境變數
ENV SERVICE_PORT=5001

# 設定工作目錄
WORKDIR /app

# 直接添加 server.py 和 requirements.txt 到 /app 目錄
ADD https://raw.githubusercontent.com/4-learn/flask-hello/main/server.py /app/server.py
ADD https://raw.githubusercontent.com/4-learn/flask-hello/main/requirements.txt /app/requirements.txt

# 安裝 requirements.txt 中指定的依賴
RUN pip install -r /app/requirements.txt

# 暴露 Flask 服務的埠號
EXPOSE 5001

# 設定容器啟動時執行的命令
CMD ["python3", "server.py"]

