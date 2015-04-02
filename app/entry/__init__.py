import bcrypt
from flask import Blueprint, render_template, request, flash, redirect, url_for

from forms import LoginForm

entry = Blueprint("entry", __name__, template_folder="templates")






@entry.route("/login", methods=["POST", "GET"])
def login():
	form = LoginForm()
	salt = bcrypt.gensalt()

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

@entry.route("/logout", methods=["POST", "GET"])
def logout():
	return "you did logout"
