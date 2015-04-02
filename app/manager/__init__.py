from flask import Blueprint


manager = Blueprint("manager", __name__)

@manager.route("/")
def index():
	return "Bola"

