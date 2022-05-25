import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/signup", methods = ["GET"])
def signup():
    with open("/app/logs/log.txt","w") as f:
        f.write("(Frontend) Got signup request !")

    return render_template("signup.html")

@app.route("/listAccounts", methods = ["GET"])
def listAccount():
    response = requests.get("http://backend_host:5001/listAccounts")

    return render_template("listAccount.html", user = response.text)

if __name__ == "__main__":
    app.debug = False
    app.run(host = "0.0.0.0", port = 5001)
