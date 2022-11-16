
from . import model
import datetime
import dateutil.tz
from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

user = model.User(email="mary@example.com", name="mary")
posts = [
    model.Message(
        user=user,
        text="Test post",
        timestamp=datetime.datetime.now(dateutil.tz.tzlocal()),
    ),
    model.Message(
        user=user,
        text="Another post",
        timestamp=datetime.datetime.now(dateutil.tz.tzlocal()),
    ),
]

#Lab 4 Ex 6
# Complete the following two lines:
# email = ..
# password = ...
# Get the user with that email from the database:
#user = model.User.query.filter_by(email=email).first()
# #if user and bcrypt.check_password_hash(user.password, password):
    # The user exists and the password is correct
    # return redirect(url_for("main.index"))
    # else:
    # Wrong email and/or password
    # Complete this code to flash a message and redirect to the login form



'''

@bp.route("/")
def index_home():
    user = model.User(1, "mary@example.com", "mary")
    posts = [
        model.Message(
            1, user, "Test post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("homePage.html", posts=posts)

@bp.route("/user")
def index_user():
    user2 = model.User(2, "hans@example.com", "hans")
    posts = [
        model.Message(
            1, user2, "Test post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user2, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            3, user2, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("userProfile.html", posts=posts)

@bp.route("/message")
def index_message():
    user2 = model.User(2, "hans@example.com", "hans")
    posts = [
        model.Message(
            1, user2, "Answer", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user2, "Answer", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            3, user2, "Answer", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("userProfile.html", posts=posts)
'''
