from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BikeComputers(db.Model):
    __tablename__ = "bike_computers"
    bc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bc_material = db.Column(db.String(100))
    bc_material_desc_short = db.Column(db.String(100))
    bc_language = db.Column(db.String(5))
    bc_material_desc_long = db.Column(db.String(100))
    bc_image = db.Column(db.String(255), nullable=True)

class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), unique=False, nullable=False)
    house_number = db.Column(db.String(10), nullable=True)
    postal_code = db.Column(db.String(10), nullable=True)
    city = db.Column(db.String(120), nullable=True)
    country = db.Column(db.String(120), nullable=True)
    iban = db.Column(db.String(120), unique=True, nullable=True)

class Orders(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    bc_id = db.Column(db.Integer, db.ForeignKey('bike_computers.bc_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    @property
    def id(self):
        return self.user_id