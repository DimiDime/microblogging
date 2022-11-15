from flask import Flask

from . import main

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    app.register_blueprint(main.bp)
    return app


# This class creates the web application and registers a blueprint. 
# Blueprints if Flask are a way of dividing an application into modules, 
# so that they are easier to maintain. 


#    /usr/lab/alum/0491346/Descargas/microblog-app
#cd Descargas/microblog-app
#flask --debug run