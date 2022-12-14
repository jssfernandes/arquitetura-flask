import click
from customer.ext.database import db
from customer.ext.auth import create_user
from customer.models import Customer


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Customer(id=1, first_name="Kathrine", last_name="Curnnok", email="kcurnnok0@ow.ly"),
        Customer(id=2, first_name="Nerita", last_name="Wrench", email="nwrench1@princeton.edu"),
        Customer(id=3, first_name="Peta", last_name="Littledyke", email="plittledyke2@weather.com"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Customer.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
