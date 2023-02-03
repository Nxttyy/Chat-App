from app import app, db
from flask import render_template, request, redirect, url_for
from app.forms import ChatForm, JoinRoom, NewRoom
import secrets
from app.models import Room, Messages

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

		return redirect(url_for('room', id = room_id))
		# return render_template("room.html", form=ChatForm(), message=room_id)

	return render_template("home.html", roomJoinForm = roomJoinForm, createRoomForm = createRoomForm, title="Chat-App:Home")


@app.route("/room/<id>", methods=['GET', 'POST'])
def room(id):

	chatForm = ChatForm()
	print(1)
	if chatForm.messageSubmit.data:
		print("MSG")

		content = chatForm.textMessage.data
		_message = Messages(content = content, room_id = id)
		
		db.session.add(_message)
		db.session.commit()

		chatForm.textMessage.data = ""

	messages = Room.query.filter_by(id=id).first().messages

	return render_template("room.html", form=chatForm, title="Chat-App:Room", messages = messages)


