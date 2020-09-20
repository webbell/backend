from freenit.db import db
from peewee import TextField

Model = db.Model


class Social(Model):
    city = TextField()
    name = TextField()
