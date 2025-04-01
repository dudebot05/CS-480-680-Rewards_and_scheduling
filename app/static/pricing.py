from flask_wtf import FlaskForm
from wtforms import SubmitField

class PriceForm(FlaskForm):
    monthlySubmit = SubmitField('Start Free Trial')
    annuallySubmit = SubmitField('Start Free Trial')