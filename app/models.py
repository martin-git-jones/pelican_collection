from app.extensions import db

class PelicanBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), nullable=False)  # e.g. "A1"
    title = db.Column(db.String(255), nullable=False)
    owned = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(255))
    note = db.Column(db.Text)

    def __repr__(self):
        return f"<PelicanBook {self.number} - {self.title}>"

