import csv
from app import create_app
from app.extensions import db
from app.models import PelicanBook

app = create_app()

with app.app_context():
    with open("pelicans.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Avoid duplicates based on "number"
            existing = PelicanBook.query.filter_by(number=row['number']).first()
            #if not existing:
            if 1 == 1:
                book = PelicanBook(
                    number=row['number'],
                    title=row['title'],
                    owned=row['owned'].strip().lower() == "yes",
                    image=row['image'],
                    note=row['note']
                )
                db.session.add(book)
        db.session.commit()

print("Import complete.")

