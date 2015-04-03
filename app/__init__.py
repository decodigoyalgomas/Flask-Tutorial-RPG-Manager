from flask import Flask
from flask_zurb_foundation import Foundation
from flask.ext.login import LoginManager
from pony.orm import *


from config import DevConfig
from models import *

from app.manager.views import manager
from app.auth.views import auth
from app.api.views import api


def create_app():

    app = Flask(__name__)
    app.config.from_object(DevConfig)

    app.register_blueprint(manager)
    app.register_blueprint(auth)
    app.register_blueprint(api)

    Foundation(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(id):
        with db_session:
            user = User.get(id=id)
        return user

    return app
