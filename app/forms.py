from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class ChatForm(FlaskForm):
	textMessage = StringField("chat", validators= [ InputRequired() ] )
	messageSubmit = SubmitField('send')

class JoinRoom(FlaskForm):
	key = StringField("Key", validators = [InputRequired() ])
	joinSubmit = SubmitField('Join')

class NewRoom(FlaskForm):
	name = StringField('New Room')
	newSubmit = SubmitField('Create Room')