from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class ChatForm(FlaskForm):
    textMessage = StringField("chat", validators=[InputRequired()])
    messageSubmit = SubmitField(
        "send", render_kw={"class": "btn btn-info create-room-btn"}
    )


class JoinRoom(FlaskForm):
    key = StringField(
        "Key",
        validators=[InputRequired()],
        render_kw={
            "class": "",
            "placeholder": "Enter Room Key",
        },
    )
    joinSubmit = SubmitField("Join")


class NewRoom(FlaskForm):
    name = StringField("New Room")
    newSubmit = SubmitField(
        "Create Room", render_kw={"class": "create-room-submit"}
    )

