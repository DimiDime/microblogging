# __init__.py makes website folder to a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize new data base
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__) # File name that runs
  app.config['SECRET_KEY'] = 'lökamsdfmsadgfäsdgkljdnogvdk' # Secret key for app
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # 
  db.init_app(app) # >This is the app we are going to use

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  # url_prefix -> all URLs inside blueprint file 
  app.register_blueprint(auth, url_prefix='/')

  from .models import User, Note

  #create_database(app)
  with app.app_context():
    db.create_all()

  return app

def create_database(app):
    if not path.exists('website/' + DB_NAME): # Check if db exists
      db.create_all(app=app) # If not create db, pass app
      print('Created Database!')

