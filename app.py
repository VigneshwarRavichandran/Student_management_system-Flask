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
	# Password encryption
	hashed_password = encrypt_password(password)
	user_exist = get_check(userid)
	# Check for user existence
	if not user_exist:
		if user_role == 'professor':
			user_subjectid = data['subject_id']
			# Creating a user with professor role
			create_professor(userid, username, hashed_password, user_subjectid)
		elif user_role == 'student':
			user_departmentid = data['department_id']
			# Creating a user with student role
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
	# Check for user existence
	if user:
		hashed_password = user.encrypted_data
		# Verifing the password by decrypting it
		if verify_user(password, hashed_password):
			# Obtaining a access token
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
		userid = get_data(token)
		data = request.get_json()
		action = data['action']
		response = None
		# Professor's action to get all his/her students
		if action == 'get all students':
			professor = get_professor(userid)
			# Verify whether the user is professor
			if not professor:
				return jsonify({'message' : 'ERROR: Unauthorized user'}), 401
			response = get_all_students(professor)
		# Students's action to get all his/her subjects
		elif action == 'get all subjects':
			student = get_student(userid)
			# Verify whether the user is student
			if not student:
				return jsonify({'message' : 'ERROR: Unauthorized user'}), 401
			response = get_all_subjects(student)
		# Students's action to get all his/her professors
		elif action == 'get all professors':
			student = get_student(userid)
			# Verify whether the user is student
			if not student:
				return jsonify({'message' : 'ERROR: Unauthorized user'}), 401
			response = get_all_professors(student)
		return jsonify({
			'action' : action,
			'response' : response
			})

if __name__ == '__main__':
	app.run(debug=True)