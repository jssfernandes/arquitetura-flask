from customer.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Customer(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(140))
    last_name = db.Column(db.String(140))
    email = db.Column(db.String(140))


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
