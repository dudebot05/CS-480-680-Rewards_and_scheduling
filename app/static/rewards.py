from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class RewardsForm(FlaskForm):
    service_type = SelectField('Reward Type', choices=[
        ('discount', 'Discount'),
        ('special offer', 'Special Offer')
    ], validators=[DataRequired()])
    
    expirationDate = DateTimeField('Booking Date and Time', 
                                format='%Y-%m-%dT%H:%M',
                                validators=[DataRequired()])
    
    notes = TextAreaField('Special Notes')