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

@app.route('/')
def index():
    with app.app_context():
        db.create_all()
    
    return "OK"

if __name__ == "__main__":
    app.debug = False
    app.run(host = "0.0.0.0", port = 5001)
