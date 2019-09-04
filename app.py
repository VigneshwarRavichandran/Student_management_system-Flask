from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/student_login', methods=['POST', 'GET'])
def student_login():
	error = message
  if request.method == 'POST':
  	data = request.get_json()
  	print(data)
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        error = 'Invalid Credentials. Please try again.'
    else:
        return redirect(url_for('student'))
  return render_template('login.html', message=error)

if __name__ == '__main__':
	app.run(debug=True)