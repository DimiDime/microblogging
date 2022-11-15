import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(1, "mary@example.com", "mary")
    posts = [
        model.Message(
            1, user, "Test post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/index.html", posts=posts)




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