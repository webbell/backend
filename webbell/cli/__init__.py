import click
import csv as c
from flask.cli import AppGroup

from ..models.medic import Medic
from ..models.social import Social

csv = AppGroup('csv', short_help='Manage CSV files')


def register_csv(app):
    @csv.command()
    @click.argument('csvpath')
    def medic(csvpath):
        with open(csvpath, newline='') as csvfile:
            next(csvfile)
            csvreader = c.reader(csvfile)
            for row in csvreader:
                print(row)
                medic = Medic()
                medic.title = row[0]
                medic.name = row[1]
                medic.specialty = row[2]
                medic.academic = row[3]
                medic.city = row[4]
                medic.save()

    @csv.command()
    @click.argument('csvpath')
    def social(csvpath):
        with open(csvpath, newline='') as csvfile:
            next(csvfile)
            csvreader = c.reader(csvfile)
            for row in csvreader:
                print(row)
                social = Social()
                social.name = row[0]
                social.specialty = row[1]
                social.save()

    app.cli.add_command(csv)


def register(app):
    register_csv(app)
