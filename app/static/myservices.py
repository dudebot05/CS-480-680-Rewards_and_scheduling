from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class ServiceForm(FlaskForm):
    name = StringField('Service Name: ', validators=[DataRequired(), Length(1, 100)])
    description = TextAreaField('Description: ', validators=[Length(max=500)])
    price = FloatField('Price: $', validators=[DataRequired(), NumberRange(min=0)])
    is_active = BooleanField('Service Active')
    submit = SubmitField('Save Service')