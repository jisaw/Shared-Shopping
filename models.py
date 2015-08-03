from datetime import datetime

from sharedshopping import db

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, default="Groceries")
    creator_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(80), nullable=False)
    list_id = db.Column(db.Integer, nullable=False)
    removed = db.Column(db.Boolean, default=False)

class ListPermission(db.Model):
    list_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
