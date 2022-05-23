from flask import Flask
app = Flask(__name__)


@app.route("/", methods = ["GET"])
def home():
    return "OK"

if __name__ == "__main__":
    app.debug = False
    app.run(host = "0.0.0.0", port = 5001)
