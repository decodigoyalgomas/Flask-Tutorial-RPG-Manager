from flask import Blueprint

api = Blueprint("api", __name__)



@api.route("/api", methods=["POST"])
def addItem():
	return "posted to api"

@api.route("/api", methods=["DELETE"])
def deleteItem():
	return "deleted api"
