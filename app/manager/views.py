from flask import Blueprint, render_template


manager = Blueprint("manager", __name__, template_folder="templates")

@manager.route("/")
def index():
	return render_template("index.html")

