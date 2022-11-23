from flask import Blueprint, render_template

auth = Blueprint('auth', __name__) # Blueprint for flask application

@auth.route('/login')
def login():
  return render_template("login.html", boolean = True) #"<p>Login</p>"

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
  return render_template("signup.html")