from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

class ForgotPassForm(FlaskForm):
    email = StringField('Please enter your email: ', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Send link to email') 

    #Added by Iyona