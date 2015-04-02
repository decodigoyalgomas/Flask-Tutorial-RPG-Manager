from flask import Flask 
from flask_zurb_foundation import Foundation 


from config import DevConfig
from models import *


app = Flask(__name__)
app.config.from_object(DevConfig)

Foundation(app)

