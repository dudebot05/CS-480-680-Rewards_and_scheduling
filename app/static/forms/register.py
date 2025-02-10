from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ...models.user import User

class RegistrationForm(FlaskForm):
    username = StringField('Please enter a username: ', validators=[DataRequired(), Length(1, 64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
            'Usernames must have only letters, numbers, dots or underscores')])
    email = StringField('Please enter your email: ', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Please enter a password: ', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password: ', validators=[DataRequired()])
    submit = SubmitField('Create new account')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered')
    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')