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