import os
import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

backend_host = "http://192.168.0.100:5002"

@app.route("/signup", methods = ["GET"])
def signup():
    log_directory = "/app/logs"
    log_file_path = os.path.join(log_directory, "log.txt")

    # 檢查目錄是否存在，如果不存在，則創建它
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    with open(log_file_path, "w") as f:
        f.write("(Frontend) Got signup request !")

    return render_template("signup.html", backend_ip = backend_host)

@app.route("/listAccounts", methods = ["GET"])
def listAccount():
    response = requests.get(backend_host + "/listAccounts")

    return render_template("listAccount.html", user = response.text)

if __name__ == "__main__":
    app.debug = False
    app.run(host = "0.0.0.0", port = 5001)
