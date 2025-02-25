from flask import Flask, render_template
from .views import view_todo, view_auth

def create_app():
	app = Flask(__name__)

	#configuracion de la aplicacion
	app.config.from_mapping(
		DEBUG = True,
		SECRET_KEY = 'dev',
	)

	#Registrar blueprints

	app.register_blueprint(view_todo.bp)
	app.register_blueprint(view_auth.bp)
	@app.route('/')
	def index():
		return render_template('index.html')
	return app

