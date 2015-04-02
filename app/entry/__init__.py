import bcrypt
from flask import Blueprint, render_template, request, flash, redirect, url_for
import pony.orm as pony

from forms import LoginForm, RegisterForm
from app.models import User

entry = Blueprint("entry", __name__, template_folder="templates")






@entry.route("/login", methods=["POST", "GET"])
def login():
	form = LoginForm()
	

	if form.validate_on_submit():
		flash("Has hecho login con el user: {}".format(form.username.data))
		user = form.username
		password = bcrypt.hashpw(form.password.data, salt)
		
		return redirect(url_for("manager.index"))
	else:
		print "not validated"
		flash("Failed to login")

	return render_template(
		"login.html",
		form=form,
		
	)

@entry.route("/register", methods=["GET", "POST"])
@pony.db_session
def register():
	form = RegisterForm()
	salt = bcrypt.gensalt()

	if form.validate_on_submit():
		
		nickname = form.username.data
		password = bcrypt.hashpw(form.password.data, salt)
		name = form.name.data
		email = form.email.data
		
		

		user = User.get(email=email)
		if not user:
			user = User(
				nickname=nickname,
				email=email,
				password=password,
				name=name
			)
			redirect("/")
		else:
			flash("That email is already registered")
	
		
		

	return render_template(
		"register.html",
		form=form,
		title="RPG Manager | Register"
	)





@entry.route("/logout", methods=["POST", "GET"])
def logout():
	return "you did logout"
