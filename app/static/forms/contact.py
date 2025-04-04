from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    message = TextAreaField('Your Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send Message')
