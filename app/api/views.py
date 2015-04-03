from flask import Blueprint
from flask.ext.login import login_required
import pony.orm as pony

api = Blueprint("api", __name__)



@api.route("/api", methods=["POST"])
@login_required
@pony.db_session
def add_item():
	return "posted to api"

@api.route("/api", methods=["DELETE"])
@login_required
@pony.db_session
def delete_item():
	return "deleted api"

@api.route("/api", methods=["GET"])
@pony.db_session
def get_item():
	return "got this item"
