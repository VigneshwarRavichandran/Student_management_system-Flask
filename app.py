from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from helper import *

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		data = request.form
		username = data['username']
		password = data['password']
		user = get_user(username, password)
		if user:
			return redirect(url_for('user', userid=user.id))
		else:
			error = 'Invalid Credentials'
	return render_template('login.html', error=error)

@app.route('/user<userid>', methods=['POST', 'GET'])
def user(userid):
	details = get_details(userid)
	return render_template('user.html', details=details)

if __name__ == '__main__':
	app.run(debug=True)