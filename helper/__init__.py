from models import *

def get_user(username, password):
	user = session.query(Users).filter_by(username=username).first()
	if user and user.password == password:
		return user
	return False

def get_details(userid):
	user = session.query(UserDetails).filter_by(user_id=userid).first()
	user_details = {  
	  'user_role' : user.user_role,
	  'subject_teacher' : user.subject_teacher,
	  'class_teacher' : user.class_teacher, 
	  'student_mark' : user.student_mark, 
	  'student_class' : user.student_class,

	}
	if user.user_role == 'student':
		user_details['student_class_teacher'] = session.query(UserDetails.class_teacher).filter_by(class_teacher=user.student_class).first()
		print(session.query(UserDetails.class_teacher).filter_by(class_teacher=user.student_class).first())
	return user_details