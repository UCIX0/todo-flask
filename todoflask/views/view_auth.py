from flask import (
	Blueprint, render_template,
	request, redirect, url_for, flash
)
from icecream import ic
from werkzeug.security import generate_password_hash, check_password_hash

from ..models import User

from todoflask import db
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register/', methods=['POST', 'GET'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		user = User.query.filter_by(username=username).first()
		ic(user)
		if user:
			flash('El usuario ya existe', 'danger')
			ic('El usuario ya existe')
			return redirect(url_for('auth.register'))
		new_user = User(username, generate_password_hash(password))
		ic(new_user)
		db.session.add(new_user)
		db.session.commit()
		ic('Usuario registrado correctamente')
		flash('Usuario registrado correctamente', 'success')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html')

@bp.route('/login/')
def login():
	return render_template('auth/login.html')