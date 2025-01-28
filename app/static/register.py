from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

class RegistrationForm(FlaskForm):
    fname = StringField('Please enter your first name: ', validators=[DataRequired(), Length(1, 64)])
    lname = StringField('Please enter your last name: ', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Please enter your email: ', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Please enter a username: ', validators=[DataRequired(), Length(1, 64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
            'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Please enter a password: ', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password: ', validators=[DataRequired()])
    submit = SubmitField('Create new account')