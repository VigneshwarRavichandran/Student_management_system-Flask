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
	  'user_name' : user.user_name,
	  'subject_teacher' : user.subject_teacher,
	  'class_teacher' : user.class_teacher, 
	  'student_mark' : user.student_mark, 
	  'student_class' : user.student_class,
	}
	return user_details