from flask import Blueprint, render_template, redirect, url_for
from app.forms.booking import BookingForm

bp = Blueprint('booking', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/bookings')
def bookings():
    booking_form = BookingForm()
    return render_template('bookings.html', form=booking_form)

@bp.route('/bookings/new', methods=['GET', 'POST'])
def create_booking():
    booking_form = BookingForm()
    return render_template('bookings.html', form=booking_form)