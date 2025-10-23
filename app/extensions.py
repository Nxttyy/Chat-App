# socketio here

from flask_socketio import SocketIO, join_room

socketio = SocketIO()


@socketio.on("my event")
def handle_message(data):
    # print(data)
    # print("received message: " + data["data"])
    return


# Socket.IO event for joining a room
@socketio.on("join")
def on_join(data):
    # print("new join")
    room_id = data["room_id"]
    join_room(room_id)
