from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
#from jobplus.models import Company, User
#from jobplus.forms import RegisterForm, LoginForm
#from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)

@front.route('/')
def index():
	return render_template('index.html')

@front.route('/login', methods=['GET', 'POST'])
def login():
	pass

@front.route('/register', methods=['GET', 'POST'])
def register():
	pass

#@front.route('/logout')
#@login_required
#def logout():
#	logout_outer()
#	flash("You've logged out successfully, welcome again~", 'success')
#	return redirect(url_for('.index'))