from flask import Blueprint

entry = Blueprint("entry", __name__)


@entry.route("/login")
def login():
	return "you did login"

@entry.route("/logout")
def logout():
	return "you did logout"
