from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "f25e42871b71d695e0edb0deb4404fab"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize the app with the extension
db = SQLAlchemy(app)

# db.init_app(app)
with app.app_context():
    db.create_all()
#
from app import routes
