# Main views or URL front end aspect of webpage
from flask import Blueprint, render_template, request, flash, jsonify
# This file is a blueprint of our application
# Has a lot of roots defined (buncha URLs)
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) # Blueprint for flask application


@views.route('/')
# This function will run when we go to the / root
def home():
  return render_template("home.html")

