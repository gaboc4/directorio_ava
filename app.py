from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import socket
import json

curr_ip = socket.gethostbyname(socket.gethostname())

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

app = Flask(__name__)


if 'SECRET_KEY' in os.environ:
	app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
	if curr_ip == '127.0.1.1':
		app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s' % (
		os.environ['DB_USER'], os.environ['DB_PASS'], 'localhost:3306/ava_servicios')
	else:
		app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s' % (
		os.environ['DB_USER_HEROKU'],os.environ['DB_PASS_HEROKU'], os.environ['DB_URL_HEROKU'])
else:
	with open('creds.json') as creds:
		cred = json.load(creds)
		db_user = cred['DB_USER_HEROKU']
		db_pass = cred['DB_PASS_HEROKU']
		db_url = cred['DB_URL_HEROKU']
	app.config['SECRET_KEY'] = '123456'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s' % (
		db_user, db_pass, db_url)
	
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from models import Users


@login_manager.user_loader
def load_user(user_id):
	# since the user_id is just the primary key of our user table, use it in the query for the user
	return Users.query.get(int(user_id))


# blueprint for auth routes in our app
from auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from main import main as main_blueprint

app.register_blueprint(main_blueprint)

#if __name__ == '__main__':
#    app.run()