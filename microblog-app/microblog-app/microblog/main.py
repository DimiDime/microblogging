import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


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
