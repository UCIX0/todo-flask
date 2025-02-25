from flask import Flask, render_template
from .views import view_todo, view_auth
from flask_sqlalchemy import SQLAlchemy

def create_app():
	app = Flask(__name__)
	db = SQLAlchemy()
	#configuracion de la aplicacion
	app.config.from_mapping(
		DEBUG = True,
		SECRET_KEY = 'dev',
		SQLALCHEMY_DATABASE_URI = 'sqlite:///todolist.db'
	)
	db.init_app(app)
	#Registrar blueprints

	app.register_blueprint(view_todo.bp)
	app.register_blueprint(view_auth.bp)
	@app.route('/')
	def index():
		return render_template('index.html')

	with app.app_context():
		db.create_all()

	return app

