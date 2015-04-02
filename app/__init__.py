from flask import Flask 
from flask_zurb_foundation import Foundation 


from config import DevConfig
from models import *

from app.manager import manager
from app.entry import entry
from app.api import api


app = Flask(__name__)
app.config.from_object(DevConfig)

app.register_blueprint(manager)
app.register_blueprint(entry)
app.register_blueprint(api)

Foundation(app)

