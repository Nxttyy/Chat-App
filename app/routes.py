from app import app, db
from flask import render_template, request
from app.forms import ChatForm, JoinRoom, NewRoom
import secrets
from app.models import Room

@app.route("/", methods=['GET', 'POST'])
def home():

	roomJoinForm = JoinRoom()
	createRoomForm = NewRoom()

	if createRoomForm.newSubmit.data and createRoomForm.validate_on_submit():
		
		key=secrets.token_hex(8)
		room = Room(key=key)

		db.session.add(room)
		db.session.commit()

		return render_template("home.html", roomJoinForm = roomJoinForm, createRoomForm = createRoomForm, title="Chat-App:Home", message=key)

	if roomJoinForm.joinSubmit.data and roomJoinForm.validate_on_submit():

		key = roomJoinForm.key.data
		room_id = Room.query.filter_by(key=key).first().id

		return render_template("room.html", form=ChatForm(), message=room_id)

	return render_template("home.html", roomJoinForm = roomJoinForm, createRoomForm = createRoomForm, title="Chat-App:Home")


@app.route("/room", methods=['GET', 'POST'])
def room():

	form = ChatForm()

	return render_template("room.html", form=form, title="Chat-App:Room")


