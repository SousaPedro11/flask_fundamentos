from flask import Blueprint

view_bp = Blueprint('views', __name__)

from . import routes
