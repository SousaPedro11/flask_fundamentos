from flask import Flask

app = Flask(__name__)

from app.views import view_bp

app.register_blueprint(view_bp)
