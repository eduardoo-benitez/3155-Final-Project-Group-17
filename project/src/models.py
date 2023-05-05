from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class users(db.Model):
    email = db.Column(db.String(20), nullable = False)
    passw = db.Column(db.String(20), nullable = False)
    username = db.Column(db.String(20), unique = True, nullable = False)

    activeUser = db.Column(db.Boolean, nullable = False)

    account_id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)

class posts(db.Model):
    title = db.Column(db.String(20), nullable = False)
    body = db.Column(db.Text, nullable = False)
    author = db.Column(db.String(20), ForeignKey(users.username), nullable = False)

    tag = db.Column(db.String(20))

    post_id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)