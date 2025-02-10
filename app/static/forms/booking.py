from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class BookingForm(FlaskForm):
    service_type = SelectField('Service Type', choices=[
        ('haircut', 'Haircut'),
        ('massage', 'Massage'),
        ('spa', 'Spa Treatment'),
        ('facial', 'Facial')
    ], validators=[DataRequired()])
    
    booking_date = DateTimeField('Booking Date and Time', 
                                format='%Y-%m-%dT%H:%M',
                                validators=[DataRequired()])
    
    notes = TextAreaField('Special Notes')