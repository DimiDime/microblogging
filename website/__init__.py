# __init__.py makes website folder to a python package
from flask import Flask

def create_app():
  app = Flask(__name__) # File name that runs
  app.config['SECRET_KEY'] = 'lökamsdfmsadgfäsdgkljdnogvdk' # Secret key for app

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  # url_prefix -> all URLs inside blueprint file 
  app.register_blueprint(auth, url_prefix='/')
  return app

