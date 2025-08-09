from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pelican_collection.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Import models so db.create_all() knows them
    from . import models
    with app.app_context():
        db.create_all()

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app

