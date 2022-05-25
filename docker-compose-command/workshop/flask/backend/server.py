from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:user1234@db_host:5432/website"

db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

@app.route('/createAll')
def index():
    with app.app_context():
        db.create_all()
    
    return "OK"

@app.route("/signup", methods = ["POST"])
def signup():
    with open("/app/logs/log.txt","w") as f:
        f.write("(Backend) Got sigup request ...")

    req_name = request.form.get("name")
    obj_user = User(name = req_name)
    db.session.add(obj_user)
    db.session.commit()

    return "OK"

@app.route("/listAccounts", methods = ["GET"])
def listAccount():
    users = User.query.all()
    list_users = []
    for obj in users:
        list_users.append(obj.name)

    return str(list_users)

if __name__ == "__main__":
    app.debug = False
    app.run(host = "0.0.0.0", port = 5001)
