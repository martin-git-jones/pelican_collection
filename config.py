import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.abspath('pelicans.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

