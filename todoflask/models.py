from todoflask import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(25), unique=True, nullable=False)
	password = db.Column(db.Text, nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password
	def __repr__(self):
		return f"<User: {self.username} >"

class todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text)
	state = db.Column(db.Boolean, default=False)


	def __init__(self, id_user, title, description, state = False):
		self.id_user = id_user
		self.title = title
		self.description = description
		self.state	= state
	def __repr__(self):
		return f"<Todo: {self.title} >"