from sqlalchemy import MetaData, Sequence

from customer.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Customer(db.Model, SerializerMixin):
    meta = MetaData()
    sequence_obj = Sequence('customer_id_seq', metadata=meta)

    id = db.Column(db.Integer, primary_key=True, default=sequence_obj)
    first_name = db.Column(db.String(140))
    last_name = db.Column(db.String(140))
    email = db.Column(db.String(140))


class User(db.Model, SerializerMixin):
    meta = MetaData()
    sequence_obj = Sequence('user_id_seq', metadata=meta)

    __tablename__ = 'USER'
    id = db.Column(db.Integer, primary_key=True, default=sequence_obj, server_default=sequence_obj.next_value())
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
