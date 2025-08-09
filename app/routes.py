from flask import Blueprint, render_template
from .models import PelicanBook

main = Blueprint('main', __name__)

@main.route("/")
def index():
    books = PelicanBook.query.all()
    return render_template("index.html", books=books)

