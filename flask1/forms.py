from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from flask1.models import User
# import email_validator as Email

class RegistrationForm(FlaskForm):
	username = StringField('Username',
							validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',
						validators=[DataRequired(),Email()])
	password = PasswordField('password',
						validators=[DataRequired(),Length(min=8)])
	confirm_pass = PasswordField('Confirm password',
						validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username already exists. Please choose another one.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already exists.')

class LoginForm(FlaskForm):

	email = StringField('Email',
						validators=[DataRequired(),Email()])
	password = PasswordField('password',
						validators=[DataRequired(),Length(min=8)])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')



