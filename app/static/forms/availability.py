from flask_wtf import FlaskForm
from wtforms import DateField, DateTimeLocalField, StringField, DateTimeField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class AvailabilityForm(FlaskForm):
    availablefrom = DateTimeLocalField('Available from:')
    availableto = DateTimeLocalField('Available to:')
    submit = SubmitField()