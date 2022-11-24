# Define data base models!!!

from . import db # import data base from current package (Website folder)
from flask_login import UserMixin # Give user object specific ligin ability
from sqlalchemy.sql import func

# 
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Increments ids automatically
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func gets current day and time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Find out from who the note is by looking at user_id
    # One to many relationship -> One user with any notes
    # Store foreignKey on a child object that references a parent object

# Define (name of model, operation)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # Unique identifier that represents an object individually
    email = db.Column(db.String(150), unique=True) # max length 150 chars, unique -> no user can have the same mail as any other user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # Creates a list with all different notes, uses Class name 