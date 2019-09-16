from flask import request, Flask, jsonify
from passlib.hash import sha256_crypt
from helper import *
import jwt

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
		data = request.get_json()
		username = data['username']
		password = data['password']
		hashed_password = sha256_crypt.encrypt(password)

@app.route('/profile', methods=['POST', 'GET'])
def user(userid):
	details = get_details(userid)
	return render_template('user.html', details=details)

if __name__ == '__main__':
	app.run(debug=True)