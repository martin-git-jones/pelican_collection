from flask import Flask
from .extensions import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)

    # Blueprints
    from .books.routes import books_bp
    app.register_blueprint(books_bp, url_prefix="/books")

    @app.route("/")
    def index():
        return "Pelican Collection Home"

    return app
