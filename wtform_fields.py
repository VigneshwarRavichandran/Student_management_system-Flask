from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
	""" Login form """
	username = StringField('username_label', validators=[InputRequired(message="Username required")])
	password = PasswordField('password_label', validators=[InputRequired(message="Password required")])
	submit_button = SubmitField('Login')