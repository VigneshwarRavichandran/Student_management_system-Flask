from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from models import TempUsers

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
	message = None
	if request.method == 'POST':
		data = request.form
		username = data['username']
		# if request.form['username'] != 'admin' or request.form['password'] != 'admin':
		# 	message = 'Invalid Credentials. Please try again.'
		# else:
		# 	return True
			# return redirect(url_for('student'))
	return render_template('login.html', message=message)


if __name__ == '__main__':
	app.run(debug=True)