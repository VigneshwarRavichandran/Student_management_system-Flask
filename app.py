from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/student_login', methods=['POST', 'GET'])
def student_login():
	message = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			message = 'Invalid Credentials. Please try again.'
		else:
			return True
			# return redirect(url_for('student'))
	return render_template('login.html', login='Student Login', message=message)

@app.route('/staff_login', methods=['POST', 'GET'])
def staff_login():
	message = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			message = 'Invalid Credentials. Please try again.'
		else:
			return True
			# return redirect(url_for('student'))
	return render_template('login.html', login='Staff Login', message=message)

@app.route('/admin_login', methods=['POST', 'GET'])
def admin_login():
	message = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			message = 'Invalid Credentials. Please try again.'
		else:
			return True
			# return redirect(url_for('student'))
	return render_template('login.html', login='Admin Login', message=message)


if __name__ == '__main__':
	app.run(debug=True)