from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)

    from app.views import view_bp

    app.register_blueprint(view_bp)

    from app.models import cliente_model
    return app
