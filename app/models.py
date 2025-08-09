from .extensions import db
from datetime import datetime

class PelicanBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publication_date = db.Column(db.String(50))  # Store as string like "1963" or "July 2010"
    image_url = db.Column(db.String(300))
    purchase_cost = db.Column(db.Float)
    date_purchased = db.Column(db.Date)
    condition = db.Column(db.String(50))
    notes = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PelicanBook {self.title}>"

