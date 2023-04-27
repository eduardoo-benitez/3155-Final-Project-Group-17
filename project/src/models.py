# TODO - Create SQLAlchemy DB and model

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class users(db.Model):
    email = db.Column(db.String(20), nullable = False)
    passw = db.Column(db.String(20), nullable = False)
    username = db.Column(db.String(20), nullable = False)

    account_id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)

class posts(db.Model):
    title = db.Column(db.String(20), nullable = False)
    body = db.Column(db.blob, nullable = False)
    author = db.Column(db.Integer, ForeignKey(users.account_id), nullable = False)

    post_id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)