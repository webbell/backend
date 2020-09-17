from freenit.db import db
from peewee import TextField

Model = db.Model


class Medic(Model):
    academic = TextField()
    city = TextField()
    name = TextField()
    specialty = TextField()
    title = TextField()
