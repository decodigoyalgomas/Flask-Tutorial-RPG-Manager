from datetime import date
from datetime import time
from datetime import timedelta
from pony.orm import *

from werkzeug.security import generate_password_hash, check_password_hash

db = Database()

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    email = Required(unicode, unique=True)
    password = Required(unicode)
    name = Required(unicode)
    username = Optional(unicode, unique=True)
    parties = Set("Party")
    sessions = Set("Session")
    characters = Set("Character")

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class Party(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(unicode)
    created = Required(date)
    game = Optional(unicode)
    users = Set(User)
    sessions = Set("Session")
    characters = Set("Character")


class Session(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(date)
    start = Optional(time)
    end = Optional(time)
    duration = Optional(timedelta)
    story = Optional(LongUnicode)
    users = Set(User)
    party = Required(Party)
    characters = Set("Character")


class Character(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    party = Required(Party)
    sessions = Set(Session)


sql_debug(True)
