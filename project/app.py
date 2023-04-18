from flask import Flask, abort, redirect, render_template, request

from src.repositories.WebsiteRepository import website_repository_singleton

from src.models import db

app = Flask(__name__)

# TODO: DB connection

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:password@localhost:3306/movies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)