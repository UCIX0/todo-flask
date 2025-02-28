from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list/')
def index():
	return 'Lista'
@bp.route('/create/')
def crear():
	return 'crear'
