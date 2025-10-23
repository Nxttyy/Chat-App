import random
import string
import uuid
from datetime import datetime

from app import db


def generate_uuid():
    return str(uuid.uuid4())


def random_username():
    suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"anon_{suffix}"


class Room(db.Model):
    __tablename__ = "rooms"

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    key = db.Column(db.String(16), unique=True, nullable=False)

    messages = db.relationship(
        "Message", backref="room", lazy=True, cascade="all, delete"
    )


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(20), nullable=True)
    content = db.Column(db.String(300), nullable=False)
    time_sent = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    room_id = db.Column(db.String(36), db.ForeignKey("rooms.id"), nullable=False)
