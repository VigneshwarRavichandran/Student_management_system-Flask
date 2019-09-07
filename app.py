from flask import Flask, render_template, redirect, url_for, request, flash
from wtform_fields import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1998@localhost/student_management'
# Change before deploying into production
app.secret_key = 'topsecret'

db = SQLAlchemy(app)
from models import User


@app.route('/login', methods=['POST', 'GET'])
def login():

	# Create LoginForm object
	login_form = LoginForm()

	message = None

	# Validating the input
	if login_form.validate_on_submit():
		if login_form.username.data != 'admin' or login_form.password.data != 'admin': 
			# If credentials are wrong then flash message
			flash('Invalid Credentials. Please try again.')
			return redirect(url_for('login'))
		else:
			# If credentials are valid
			return redirect(url_for('student'))
	return render_template('login.html', login='Student Login', form=login_form)


if __name__ == '__main__':
	app.run(debug=True)