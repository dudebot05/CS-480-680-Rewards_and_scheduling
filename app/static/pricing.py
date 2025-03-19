from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, FileField, SubmitField, ValidationError, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Regexp
from flask_wtf.file import FileAllowed, FileRequired

class PriceForm(FlaskForm):
    billing_type = RadioField('Billing Type', choices=[('15','Pay monthly'),('10','Pay annually')], default='15')
    submit = SubmitField('Start Free Trial')