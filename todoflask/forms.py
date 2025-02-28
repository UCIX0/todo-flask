from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Usuario',
		validators=[
			DataRequired(),
			Length(min=4, max=20, message="El nombre de usuario debe tener entre 4 y 20 caracteres."),
			Regexp('^[A-Za-z0-9_]+$', message="Solo letras, números y guiones bajos.")
		])

	password = PasswordField('Contraseña',
		validators=[
			DataRequired(),
			Length(min=8, message="La contraseña debe tener al menos 8 caracteres."),
			Regexp(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).+$',
				message="Debe incluir una mayúscula, minúscula, número y un carácter especial.")
		])

	confirm_password = PasswordField('Confirmar Contraseña',
		validators=[
			DataRequired(),
			EqualTo('password', message="Las contraseñas deben coincidir.")
		])

	submit = SubmitField('Registrarse')
