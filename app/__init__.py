import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .extensions import socketio

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.secret_key = os.getenv("SECRET_KEY")

    db.init_app(app)
    socketio.init_app(app)
    from app.routes import main  # import blueprint, not app

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    from app import routes

    return app
