from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    phone = db.Column(db.String(40))
    birthday = db.Column(db.Date())
    email = db.Column(db.String(40),unique = True)
    password = db.Column(db.String(256))
