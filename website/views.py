# Main views or URL front end aspect of webpage
from flask import Blueprint
# This file is a blueprint of our application
# Has a lot of roots defined (buncha URLs)

views = Blueprint('views', __name__) # Blueprint for flask application

@views.route('/')
# This function will run when we go to the / root
def home():
  return "<h1>Test</h1>"

