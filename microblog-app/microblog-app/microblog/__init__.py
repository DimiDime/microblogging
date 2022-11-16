from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
login_manager = LoginManager()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqldb://23_webapp_21:koxxNNpA@mysql.lab.it.uc3m.es/23_webapp_21a"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Inside create_app:
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from . import model
    @login_manager.user_loader
    def load_user(user_id):
        return model.User.query.get(int(user_id))

    # Register blueprints:
    from . import main
    from . import auth
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    
    return app


'''
from flask import Flask

from . import main

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    app.register_blueprint(main.bp)
    return app
'''

# This class creates the web application and registers a blueprint. 
# Blueprints if Flask are a way of dividing an application into modules, 
# so that they are easier to maintain. 
