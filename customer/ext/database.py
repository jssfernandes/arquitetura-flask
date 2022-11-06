from flask_sqlalchemy import SQLAlchemy
import cx_Oracle
import os


db = SQLAlchemy()

def init_app(app):
    username = os.environ.get('db_username')
    password = os.environ.get('db_password')
    dsn_name = os.environ.get('dsn_name')
    tns_dir = os.environ.get('tns_admin')
    cx_Oracle.init_oracle_client(lib_dir=tns_dir)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'oracle://{username}:{password}@{dsn_name}'
    db.init_app(app)
