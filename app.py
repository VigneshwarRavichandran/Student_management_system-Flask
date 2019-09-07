from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1998@localhost/student_management'

db = SQLAlchemy(app)

class Temp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)

@app.route('/login', methods=['POST', 'GET'])
def login():
	message = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			message = 'Invalid Credentials. Please try again.'
		else:
			return True
			# return redirect(url_for('student'))
	return render_template('login.html', message=message)

if __name__ == '__main__':
	app.run(debug=True)