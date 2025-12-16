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
    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), unique=False, nullable=False)
    iban = db.Column(db.String(120), unique=True, nullable=False)
    
    @property
    def id(self):
        return self.user_id