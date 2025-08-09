from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    publication_date = db.Column(db.String(50))  # Keep as string for flexible formats
    image_filename = db.Column(db.String(255))
    purchase_cost = db.Column(db.Float)
    date_purchased = db.Column(db.Date)
    condition = db.Column(db.String(50))
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
