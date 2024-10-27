import secrets

from flask import redirect, render_template, url_for

from app import app, db
from app.forms import ChatForm, JoinRoom, NewRoom
from app.models import Messages, Room

from .extensions import socketio

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    roomJoinForm = JoinRoom()
    createRoomForm = NewRoom()

    if createRoomForm.newSubmit.data and createRoomForm.validate_on_submit():
        key = secrets.token_hex(8)
        room = Room(key=key)

        db.session.add(room)
        db.session.commit()
        print(f"room {key} created!")

        return render_template(
            "home.html",
            roomJoinForm=roomJoinForm,
            createRoomForm=createRoomForm,
            title="Chat-App:Home",
            message=key,
        )

    if roomJoinForm.joinSubmit.data and roomJoinForm.validate_on_submit():
        key = roomJoinForm.key.data

        if key:
            room = Room.query.filter_by(key=key).first()
            if room:
                room_id = room.id
                return redirect(url_for("room", id=room_id))
            else:
                print("Room ID not found!")
        else:
            print("Key not found!")
    # return render_template("room.html", form=ChatForm(), message=room_id)
    return render_template(
        "home.html",
        roomJoinForm=roomJoinForm,
        createRoomForm=createRoomForm,
        title="Chat-App:Home",
    )


@app.route("/room/<id>", methods=["GET", "POST"])
def room(id):
    chatForm = ChatForm()
    if chatForm.messageSubmit.data:
        content = chatForm.textMessage.data
        _message = Messages(content=content, room_id=id)

        db.session.add(_message)
        db.session.commit()

        chatForm.textMessage.data = ""

        # Emit the message to all users in the specific room without additional filtering
        # print(f"emmited {id}")
        socketio.emit(
            "new_message",
            {
                "content": _message.content,
                "time_sent": _message.time_sent.strftime("%m/%d/%Y, %H:%M:%S"),
            },
            room=id,
        )

    messages = Room.query.filter_by(id=id).first().messages
    message_count = len(messages)

    return render_template(
        "room.html",
        form=chatForm,
        title="Chat-App:Room",
        messages=messages,
        room_id=id,
        message_count=message_count,
    )
