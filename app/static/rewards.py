from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SelectField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class RewardsForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired(), Length(1, 64)])
    service_type = SelectField('Reward Type: ', choices=[
        ('discount', 'Discount'),
        ('special offer', 'Special Offer')
    ], validators=[DataRequired()])
    
    points = IntegerField('Points needed: ', validators=[DataRequired()])
    description = TextAreaField('Description: ', validators=[DataRequired()])
    submit = SubmitField('Create Reward')