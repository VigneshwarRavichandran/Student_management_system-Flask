from flask import request, Flask, jsonify
from helper import *

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	userid = data['userid']
	username = data['username']
	password = data['password']
	user_role = data['role']
	hashed_password = encrypt_password(password)
	user_exist = get_check(userid)
	if not user_exist:
		if user_role == 'professor':
			user_subjectid = data['subject_id']
			create_professor(userid, username, hashed_password, user_subjectid)
		elif user_role == 'student':
			user_departmentid = data['department_id']
			create_student(userid, username, hashed_password, user_departmentid)
		return jsonify({
		'message' : 'User registered successfully'
		})
	return jsonify({
	'message' : 'User already exists'
	})

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	userid = data['userid']
	password = data['password']
	user = get_user(userid)
	if user:
		hashed_password = user.encrypted_data
		if verify_user(password, hashed_password):
			token = get_token(userid)
			return jsonify({
				'token' : token
			  })
		return jsonify({
			'message' : 'Incorrect Password'
		})
	return jsonify({
		'message' : 'Invalid userid'
		})

@app.route('/profile', methods=['POST', 'GET'])
def profile():
	if request.method == 'GET':
		token = request.headers['token']
		data = get_data(token)
		hashed = request.get_json()
		return jsonify({
			'data' : data,
			'hashed' : hashed
			})

if __name__ == '__main__':
	app.run(debug=True)