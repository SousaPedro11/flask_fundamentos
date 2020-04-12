from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app=app)

from app.views import view_bp

app.register_blueprint(view_bp)
