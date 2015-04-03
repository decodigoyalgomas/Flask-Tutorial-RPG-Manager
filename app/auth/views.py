
from flask import Blueprint, render_template, request,\
    flash, redirect, url_for, session, current_app, g
from flask.ext.login import current_user, login_user, \
    logout_user, login_required

import pony.orm as pony
import pprint

from forms import LoginForm, RegisterForm
from app.models import User



auth = Blueprint("auth", __name__, template_folder="templates")




@auth.before_request
def get_current_user():
    g.user = current_user

@auth.route("/register", methods=["POST", "GET"])
@pony.db_session
def register():
    
    if session.get("username"):
        flash("Youur are already logged in", "info")
        redirect(url_for("manager.index"))

    form = RegisterForm()
    if form.validate_on_submit():
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
        email = request.form.get("email")

        existing_username = User.get(username=username)
        if existing_username:
            flash(
                "Username {} already existst in the database".format(username), "error")
            return render_template("register.html", form=form)

        user = User(
            username=username,
            name=name,
            email=email,
            password=password
        )
        flash('You are now registered. Please login.', 'success')
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth.route("/login", methods=["POST", "GET"])
@pony.db_session
def login():
    if current_user.is_authenticated():
        flash("You are already logged in", "success")
        return redirect(url_for("manager.index"))
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
        email = request.form.get("email")

        existing_user = User.get(username=username)
        if not (existing_user and existing_user.check_password(password)):
            flash('Invalid username or password. Please try again.', 'danger')
            return render_template('login.html', form=form)

        login_user(existing_user)
        flash('You have successfully logged in.', 'success')
        return redirect(url_for('manager.index'))
    if form.errors:
        flash(form.errors, 'danger')

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('manager.index'))
