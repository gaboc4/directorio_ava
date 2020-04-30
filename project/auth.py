# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import Users
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
	return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
	email = request.form.get('email')
	password = request.form.get('password')
	remember = True if request.form.get('remember') else False

	user = Users.query.filter_by(email=email).first()

	if not user or not check_password_hash(user.password, password):
		flash('Please check your login details and try again.')
		return redirect(url_for('auth.login'))

	# if the above check passes, then we know the user has the right credentials
	login_user(user, remember=remember)
	return redirect(url_for('main.profile'))


@auth.route('/reset_password')
def reset_password():
	return render_template('reset_password.html')


@auth.route('/reset_password', methods=['POST'])
def reset_password_post():
	email = request.form.get('email')
	password1 = request.form.get('new_password1')
	password2 = request.form.get('new_password2')
	if password1 != password2:
		flash('Passwords did not match please try again.')
		return redirect(url_for('auth.reset_password'))
	user = Users.query.filter_by(email=email).first()

	user.password = generate_password_hash(password1, method='sha256')
	db.session.commit()
	flash('Password reset successfully!')
	return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
	return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
	email = request.form.get('email')
	first_name = request.form.get('first_name')
	last_name = request.form.get('last_name')
	password = request.form.get('password')
	user_type = request.form.get('user_type')

	user = Users.query.filter_by(email=email).first()

	if user:
		flash('Email address already exists')
		return redirect(url_for('auth.signup'))

	# create new user with the form data. Hash the password so plaintext version isn't saved.
	new_user = Users(email=email, first_name=first_name, last_name=last_name,
	                 password=generate_password_hash(password, method='sha256'))

	db.session.add(new_user)
	db.session.commit()

	return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))
