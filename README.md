# Pelican Book Collection

A Flask web application to catalog and display my collection of Pelican Books.
Includes:
- Search by title or author
- Filter by ownership status
- Responsive, clean design

This project was developed collaboratively with ChatGPT as a coding assistant.
I documented each step of the process in the `/docs` folder.

## Features
- Python + Flask backend
- SQLite database via SQLAlchemy
- CSV import for bulk book entry
- Search & filter interface
- Mobile-friendly layout

## Getting Started
1. Clone this repo:
git clone https://github.com/martin-git-jones/pelican_collection.git

2. Install dependencies:
pip install -r requirements.txt

3. Initialize the database:
flask db upgrade

4. Import books from CSV:
flask run

Developed with ChatGPT

This project was built in close collaboration with ChatGPT as an AI coding partner.
The process followed an iterative, test-driven approach:

    Defining the goal – I explained the vision: a searchable, filterable, visually clean web app to catalog my Pelican Book collection, starting from a CSV file.

    Incremental development – ChatGPT generated small, focused code snippets for each step:

        Setting up a Flask app and SQLite database with SQLAlchemy models

        Creating a CSV import script

        Building routes and Jinja templates for displaying books

        Adding instant client-side search and filtering

        Styling with responsive, modern CSS

    Debugging together – When errors occurred (e.g., missing imports, database schema mismatches), I shared the traceback and ChatGPT helped identify and fix the problem.

    Feature expansion – We added enhancements like a search bar, ownership filter, and flexible layout.

    Documentation and polish – I asked ChatGPT to create documentation, clean code, and suggest usability improvements.

By working this way, I was able to:

    Ship a fully functional application much faster

    Maintain full understanding of the codebase

    Learn new Flask, SQLAlchemy, and front-end techniques in the process

This project demonstrates my ability to:

    Break down requirements into manageable tasks

    Collaborate with AI tools effectively

    Build clean, maintainable, and user-friendly applications from scratch
