""" Authentication Model """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flaskblog import app, db
from flaskblog.models import User


class RegistrationForm(FlaskForm):
  """ RegistrationForm Class that let's user for creating a new account """
  username = StringField('Username',
                         validators=[DataRequired(), Length(min=5, max=20)])
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password',
                           validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password',
                           validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
    with app.app_context():
      user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('That username is taken. please choose a diffrent one.')

  def validate_email(self, email):
    with app.app_context():
      user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('That email is taken. please choose a diffrent one.')


class LoginForm(FlaskForm):
  """ LoginForm Class that let's user to access to thir account """
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password',
                           validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')