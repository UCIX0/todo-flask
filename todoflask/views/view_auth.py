from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register/')
def index():
	return 'Registro'

@bp.route('/login/')
def crear():
	return 'Login'