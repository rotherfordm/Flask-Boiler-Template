from config import Config

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, desc, or_, and_

from flask import abort, flash, g, jsonify, redirect, render_template, request, url_for
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

from werkzeug.urls import url_parse
from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename

from uuid import uuid4

import json
import urllib.request

from app import app, db
from app.models import User

CORS(app)

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

auth = HTTPBasicAuth()

@app.before_first_request
def create_database():
    db.create_all()
    db.session.commit()


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@app.route("/api/users", methods=["POST"])
# @auth.login_required
def new_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400)  # existing user
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return (
            jsonify({"username": user.username}),
            201,
            {"Location": url_for("get_user", id=user.id, _external=True)},
        )

@app.route("/api/users/<int:id>")
@auth.login_required
def get_user(id):
    user = User.query.get(id)
    if not user and g.user != user:
        abort(400)
    return jsonify({"username": user.username})


@app.route("/api/token")
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify(
        {"token": token.decode("ascii"), "user_id": g.user.id, "expires_in": 3600}
    )

@app.route("/", methods=["GET", "POST"])
def index():
    return abort(418)

