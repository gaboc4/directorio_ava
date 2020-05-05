from flask_login import UserMixin
from . import db


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    email = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000))

    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Business(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    owner_id = db.Column(db.Integer)
    business_email = db.Column(db.String(1000))
    phone_number = db.Column(db.String(1000))
    sector = db.Column(db.String(1000))
    address = db.Column(db.String(1000))
    description = db.Column(db.String(1000000))

    def __init__(self, name, owner_id, business_email, phone_number, sector, address, description):
        self.name = name
        self.owner_id = owner_id
        self.business_email = business_email
        self.phone_number = phone_number
        self.sector = sector
        self.address = address
        self.description = description
