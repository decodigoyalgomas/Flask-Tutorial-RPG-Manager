from flask.ext.wtf import Form
from flask.ext.wtf.html5 import EmailField
from wtforms import TextField, PasswordField, SubmitField, validators 
from wtforms.validators import Required, Email 

class LoginForm(Form):
	username = TextField("user", validators=[Required("Enter your Username")])
	password = PasswordField("password", validators=[Required("Enter your Password")])
	submit = SubmitField("submit")