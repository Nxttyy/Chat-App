from app import db
from datetime import datetime

class Room(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	key = db.Column(db.String(16), unique=True, nullable=False)
	messages = db.relationship('Messages', backref='room')

class Messages(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(300), unique=False, nullable=False)
	time_sent = db.Column(db.DateTime ,nullable=False ,default=datetime.utcnow)
	room_id = db.Column(db.Integer, db.ForeignKey('room.id'))


