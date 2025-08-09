# Pelican Collection Website – Development Log

## Project Overview
This project is a personal website for cataloguing my Pelican book collection.  
It is intended to:
- Look visually appealing.
- Be modular and extendable over time.
- Serve as a public example of my Python + Flask development skills.
- Demonstrate how I have integrated ChatGPT into my development workflow.

## ChatGPT Collaboration – Step 1
**Date:** 2025-08-09  
**Goal:** Set up an initial, well-structured Flask project scaffold.

### Prompt to ChatGPT:
> I have a collection of Pelican books and want to use ChatGPT to build a website. I want to put the code in GitHub and use this project as an example of my work when job hunting.
> I want to record the details such as Title, Author, Publication Date, Image, Purchase Cost, Date Purchased, Condition, Notes.
> I want the website to look good and for it to record how I used ChatGPT to develop the code.
> I was thinking Python and Flask. I would like it to be very modular and extend with new features over time.
> I have a simple record of my collection in Wordpress here:
> http://mailpony.uk/wordpress/pelicans/
> 
> How do you recommend I showcase this project?

### ChatGPT Response Summary:
- Suggested a modular Flask app structure using **Flask Blueprints**.
- Proposed use of **SQLAlchemy ORM** with SQLite initially.
- Created:
  - Project folder layout.
  - `requirements.txt` with initial dependencies.
  - Base SQLAlchemy `Book` model.
  - Flask app factory in `app/__init__.py`.
  - Config file for environment-based settings.
  - A "books" blueprint with a simple list route.
  - Example HTML template for listing books.
- Recommended including a `/docs` folder to record the ChatGPT-assisted development process.

### Implementation:
I copied ChatGPT’s initial scaffold into the repository and created:
- `app/` folder with base code.
- `requirements.txt` for package dependencies.
- `docs/development-log.md` (this file) to record progress.

---

## Next Planned Steps:
1. Add `base.html` template and basic styling (Bootstrap or Tailwind).
2. Implement CRUD routes for books (Add, Edit, Delete).
3. Integrate image uploads for book covers.
4. Add unit tests under `tests/`.
5. Record each ChatGPT-assisted step in this development log.

---

## Notes:
By logging my ChatGPT prompts and its responses, I am showing:
- My ability to collaborate effectively with AI tools.
- How I can translate AI suggestions into real code.
- A transparent record of project evolution.


