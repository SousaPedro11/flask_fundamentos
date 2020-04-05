from app.views import view_bp


@view_bp.route('/')
def index():
    return "Olá Flask"
