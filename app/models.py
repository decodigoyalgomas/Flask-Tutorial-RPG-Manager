from datetime import date
from datetime import time
from datetime import timedelta
from pony.orm import *

db = Database()

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    email = Required(unicode, unique=True)
    password = Required(unicode)
    name = Required(unicode)
    nickname = Optional(unicode)
    parties = Set("Party")
    sessions = Set("Session")
    characters = Set("Character")


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
