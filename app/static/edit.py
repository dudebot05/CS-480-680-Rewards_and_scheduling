from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, FileField, SubmitField, ValidationError, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Regexp
from flask_wtf.file import FileAllowed, FileRequired

class EditForm(FlaskForm):
    username = StringField('Enter your new username: ', validators=[DataRequired(), Length(1, 64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
            'Usernames must have only letters, numbers, dots or underscores')])
    account_type = RadioField('Account Type', choices=[('Customer'),('Owner')])
    profile_pic = FileField(validators=[FileRequired(), FileAllowed(['jpg','png'], 'Only .jpg or .png')])
    submit = SubmitField('Save changes')