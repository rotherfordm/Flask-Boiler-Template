from config import Config

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, desc

from flask import render_template, flash, redirect, url_for, request, Flask, jsonify

from werkzeug.urls import url_parse
from werkzeug.exceptions import HTTPException

from app import app, db
from app.models import Calculation

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

@app.before_first_request
def create_database():
    db.create_all()
    db.session.commit()


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    return jsonify({}, 200)

@app.route("/test", methods=["GET", "POST"])
def test():
    user = User()
    user.name = "John"
    user.id = 1
    return jsonify(name=user.name, id=user.id, status=200)

class User(object):
    name = None
    id = None