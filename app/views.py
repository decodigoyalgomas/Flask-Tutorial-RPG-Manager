
from app import app



@app.route("/")
def index():
	return "Bola"

@app.route("/login")
def login():
	return "login"

@app.route("/logout")
def logout():
	return "logout"

@app.route("/<user>")
def user(user):
	return user

@app.route("/<user>/admin")
def admin_panel(user):
	return "This is your admin panel dear {}".format(user)

@app.route("/character", methods=["POST", "DELETE"])
def character(user):
	return "list of your characters"

@app.route("/party", methods=["POST", "DELETE"])
def party(user):
	return "This is your party"