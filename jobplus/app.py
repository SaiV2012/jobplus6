from flask import Flask
from flask_migrate import Migrate
from jobplus.config import configs
#from jobplus.models import db, User, Company
#from flask_login import LoginManager

def register_extensions(app):
	pass

def register_blueprints(app):
	from .handlers import front, admin, companies, users
	app.register_blueprint(front)
	app.register_blueprint(admin)
	app.register_blueprint(companies)
	app.register_blueprint(users)

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(configs.get(config))
	#register_extensions(app)
	register_blueprints(app)
	return app