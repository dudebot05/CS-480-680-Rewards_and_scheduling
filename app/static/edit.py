from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class EditForm(FlaskForm):
    username = StringField('Enter your new username: ', validators=[DataRequired(), Length(1, 64), 
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
            'Usernames must have only letters, numbers, dots or underscores')])
    submit = SubmitField('Save changes')