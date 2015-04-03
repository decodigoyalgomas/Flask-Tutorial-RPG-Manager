from flask import Blueprint, render_template, session
from flask.ext.login import login_required
import pony.orm as pony

from app.models import User

manager = Blueprint("manager", __name__, template_folder="templates")

@manager.route("/")
@login_required
@pony.db_session
def index():
	user = User.get(id=session["user_id"])
	return render_template(
		"index.html",
		user=user
	)

@manager.route("/parties", methods=["GET"])
@login_required
@pony.db_session
def my_parties():
	return render_template("parties.html")


@manager.route("/characters", methods=["GET"])
@login_required
@pony.db_session
def my_characters():
	return render_template("characters.html")

@manager.route("/list/characters")
@pony.db_session
def list_characters():
	return render_template("list_characters.html")

@manager.route("/list/parties")
@pony.db_session
def list_parties():
	return render_template("list_parties.html")


@manager.route("/characters/<string:name>")
@login_required
@pony.db_session
def character(name):
	return render_template(
		"character.html",
		name=name
	)


@manager.route("/parties/<int:id>")
@login_required
@pony.db_session
def party(id):
	return render_template(
		"party.html",
		id=id

	)


@manager.route("/new_party")
@login_required
@pony.db_session
def new_party():
	return render_template("new_party.html")

@manager.route("/new_character")
@login_required
@pony.db_session
def new_character():
	return render_template("new_character.html")

