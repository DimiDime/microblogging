from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_login

from . import db, bcrypt
from . import models

auth = Blueprint('auth', __name__)






@auth.route("/register")
def register():
    return render_template("register.html")


@auth.route("/register", methods=['POST'])
def register_post():

    email = request.form.get("email")
    password=request.form.get("password")
    #Check that passwords are equal
    if password != request.form.get("password_repeat"):
        flash("Sorry, passwords are different")
        return redirect(url_for("auth.register"))
    # Check if the email is already at the database
    user = models.User.query.filter_by(email=email).first()
    if user:
        flash("Sorry, the email you provided is already registered", category="error")
        return redirect(url_for("auth.register"))
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = models.User(email=email, password=password_hash, role="1")
    db.session.add(new_user)
    db.session.commit()
    flash("You've successfully signed up!", category="success")

    return redirect(url_for("views.home"))
    

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login',methods=['POST'])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    # Get the user with that email from the database:
    user = models.User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
    # The user exists and the password is correct
        flask_login.login_user(user)
        return redirect(url_for("views.home"))
    else:
    # Wrong email and/or password
    # Complete this code to flash a message and redirect to the login form
  
        flash("Sorry, password or email is wrong", category="error")
        return redirect(url_for("auth.login"))



@auth.route("/logout", methods=["GET","POST"])
@flask_login.login_required
#POST REQUEST
def logout():
    flask_login.logout_user()
    return redirect(url_for("auth.login"))
