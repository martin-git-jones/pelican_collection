from flask import Blueprint, render_template
from .models import PelicanBook

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    books = PelicanBook.query.all()
    return render_template("index.html", books=books)

