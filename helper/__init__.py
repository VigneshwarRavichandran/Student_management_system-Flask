from passlib.hash import sha256_crypt
from models import *
import jwt

def check_user(userid):
	user = session.query(Users).filter_by(id=userid).first()
	if user:
		return True
	return False

def create_professor(userid, username, hashed_password, user_subjectid):
	user = Users(id=userid, encrypted_data=hashed_password)
	session.add(user)
	professor = Professors(id=userid, name=username, subject_id=user_subjectid)
	session.add(professor)
	session.commit()

def create_student(userid, username, hashed_password, user_departmentid):
	user = Users(id=userid, encrypted_data=hashed_password)
	session.add(user)
	student = Students(id=userid, name=username, department_id=user_departmentid)
	session.add(student)
	session.commit()

def get_user(userid):
	user = session.query(Users).filter_by(id=userid).first()
	if user:
		return user
	return False

def encrypt_paddword(password):
	hashed_password = sha256_crypt.encrypt(password)
	return hashed_password

def verify_user(password, hashed_password):
	if sha256_crypt.verify(password, hashed_password):
		return True
	return False

def get_token(userid):
	access_token = jwt.encode({'userid' : userid}, 'secret', algorithm='HS256')
	token = access_token.decode('utf-8')
	return token

def get_data(token):
	access_token = token.encode('utf-8')
	data = jwt.decode(access_token, 'secret')
	return data['userid']

def get_professor(userid):
	professor = session.query(Professors).filter_by(id=userid).first()
	if professor:
		return professor
	return False

def get_student(userid):
	student = session.query(Students).filter_by(id=userid).first()
	if student:
		return student
	return False

def get_all_students(professor):
	subject_id = professor.subject_id
	department_id = session.query(Subjects.department_id).filter_by(id=subject_id).first()
	students = session.query(Students.id, Students.name).filter_by(department_id=department_id).all()
	return students

def get_all_subjects(student):
	department_id = student.department_id
	subjects = session.query(Subjects.id, Subjects.name).filter_by(department_id=department_id).all()
	return subjects

def get_all_professors(student):
	department_id = student.department_id
	subjects = session.query(Subjects.id).filter_by(department_id=department_id).all()
	professors = []
	for subject in subjects:
		professor = session.query(Professors.name, Professors.subject_id).filter_by(subject_id=subject).first()
		professors.append(professor)
	return professors