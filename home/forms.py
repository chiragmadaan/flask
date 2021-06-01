from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from home.models import Users


class RegistrationForm(FlaskForm):
	firstname = StringField(label='First Name', validators=[Length(min=2, max=15), DataRequired()])
	lastname = StringField(label='Last Name', validators=[Length(min=0, max=15)])
	phone_number = StringField(label='Contact Number', validators=[Length(max=10)])
	email = StringField(label='Email ID', validators=[Email(), DataRequired()])
	password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
	password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
	submit = SubmitField(label='Create Account')

	def validate_email(self, email_entered):
		user = Users.query.filter_by(email=email_entered.data).first()
		if user:
			raise ValidationError('Email ID already exists, please try a different Email ID')


class LoginForm(FlaskForm):
	email = StringField(label='Email ID', validators=[Email(), DataRequired()])
	password = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
	submit = SubmitField(label='Log In')
