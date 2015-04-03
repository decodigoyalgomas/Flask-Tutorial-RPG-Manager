from flask.ext.wtf import Form
from flask.ext.wtf.html5 import EmailField
from wtforms import TextField, PasswordField, SubmitField, validators 
from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
	username = TextField("user", validators=[Required("Enter your Username")])
	password = PasswordField("password", validators=[Required("Enter your Password")])
	submit = SubmitField("submit")

class RegisterForm(LoginForm):
	email = EmailField("email", validators=[Required("enter an email"), Email("Enter a valid email")])
	name = TextField('name', validators=[Required("Enter your Name")])
	confirm = PasswordField("confirm password", validators=[Required("Enter your password again"), EqualTo("password", message="Does not match password field.")])