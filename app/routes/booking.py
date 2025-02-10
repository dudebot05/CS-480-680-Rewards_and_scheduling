from flask import render_template, redirect, url_for
from . import main
from ..static.forms.booking import BookingForm

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/bookings')
def bookings():
    booking_form = BookingForm()
    return render_template('bookings.html', form=booking_form)

@main.route('/bookings/new', methods=['GET', 'POST'])
def create_booking():
    booking_form = BookingForm()
    return render_template('bookings.html', form=booking_form)