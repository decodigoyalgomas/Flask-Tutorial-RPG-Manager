import os
from pony.orm import *

from models import db 



class Config(object):
	SECRET_KEY = os.urandom(46)


class DevConfig(Config):
	DEBUG = True
	db.bind('sqlite', 'devel.db', create_db=True)
	db.generate_mapping(create_tables=True)


class ProdConfig(Config):
	DEBUG = False
	# db.bind('postgres', user='', password='', host='', database='')

