from icecream import ic
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

ic.disable()
db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	#configuracion de la aplicacion
	app.config.from_mapping(
		DEBUG = True,
		SECRET_KEY = 'dev',
		SQLALCHEMY_DATABASE_URI = 'sqlite:///todolist.db'
	)
	if app.config['DEBUG']:
		ic.enable()
	db.init_app(app)
	#Registrar blueprints
	from .views import view_todo, view_auth
	app.register_blueprint(view_todo.bp)
	app.register_blueprint(view_auth.bp)
	@app.route('/')
	def index():
		return render_template('index.html')

	with app.app_context():
		db.create_all()

	return app

