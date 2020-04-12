from app.views import view_bp


@view_bp.route('/ola/')
def ola():
    return "ola"
