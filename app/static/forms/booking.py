from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import DateTimeLocalField, StringField, DateTimeField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


from app.models.services import Service

class BookingForm(FlaskForm):
    service_type = SelectField('Service Type: ', coerce=int, validators=[DataRequired()])
    date = DateTimeLocalField('Date and Time of Visit: ', validators=[DataRequired()])
    name = StringField('Your Name: ', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email Address: ', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number: ', validators=[])
    submit = SubmitField('Confirm Booking')