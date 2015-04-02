from flask import Flask 
from flask_zurb_foundation import Foundation 
from flask.ext.login import LoginManager


from config import DevConfig
from models import *

from app.manager.views import manager
from app.entry.views import auth
from app.api.views import api


app = Flask(__name__)
app.config.from_object(DevConfig)



app.register_blueprint(manager)
app.register_blueprint(auth)
app.register_blueprint(api)

Foundation(app)


