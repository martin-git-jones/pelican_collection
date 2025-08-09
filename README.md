# Pelican Collection Website

A personal website for cataloguing my **Pelican Books** collection, built with **Python** and **Flask**.  
This project is designed to be:
- Visually appealing and user-friendly.
- Modular and easily extended with new features over time.
- A public example of my development skills for job applications.
- A transparent record of how I use **ChatGPT** to assist in software development.

You can see the existing basic list here (WordPress version):  
[http://mailpony.uk/wordpress/pelicans/](http://mailpony.uk/wordpress/pelicans/)

---

## Features (Planned and Implemented)

### ✅ Implemented
- Flask application scaffold using **app factory** pattern.
- Modular folder structure with **Blueprints**.
- SQLite database via **SQLAlchemy ORM**.
- Example `Book` model with fields:
  - Title
  - Author
  - Publication Date
  - Image
  - Purchase Cost
  - Date Purchased
  - Condition
  - Notes
- Simple “list books” route and HTML template.

### 🚧 Planned
- CRUD operations for books (Add, Edit, Delete).
- Book cover image upload and storage.
- Search and filter functionality.
- Modern responsive UI (Bootstrap or Tailwind CSS).
- REST API endpoints for book data.
- Authentication for editing features.
- Data import/export (CSV, JSON).
- Unit tests under `/tests`.

---

## Technology Stack
- **Backend:** Python, Flask
- **Database:** SQLite (dev) → PostgreSQL/MySQL (prod option)
- **Frontend:** Jinja2 templates, Bootstrap/Tailwind (planned)
- **ORM:** SQLAlchemy
- **Environment:** Configurable via `.env` or environment variables
- **Version Control:** Git + GitHub

---

##

