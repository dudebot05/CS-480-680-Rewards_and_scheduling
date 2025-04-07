from functools import wraps
from app.models.availabletimes import AvailableTimes
from app.models.booking import Booking
from app.models.services import Service
from app.static.forms.availability import AvailabilityForm
from app.static.forms.myservices import ServiceForm
from .. import db
from app.models.rewards import RewardTransaction
from app.static.edit import EditForm
from app.static.rewards import RewardsForm
from app.static.forms.contact import ContactForm
from app.static.pricing import PriceForm
from . import main
from flask import flash, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from ..auth.routes import send_validate_account_email
import calendar
from flask_mailman import EmailMessage

def check_is_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_confirmed() == False:
            flash("Please confirm your account!", "warning")
            return redirect(url_for("main.inactive"))
        return func(*args, **kwargs)

    return decorated_function

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    form = AvailabilityForm()
    times = AvailableTimes.query.filter_by(user_id=current_user.id).all()
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    appointments = [{}]
    for time in times:
        availability = [
            {
                'todo' : 'Start Availability',
                'date' : time.available_start
            },
            {
                'todo' : 'End Availability',
                'date' : time.available_end
            }
        ]
    for booking in bookings:
        appointments = [
            {
                'todo' : booking.service_type,
                'date' : booking.booking_date
            }
        ]
    if form.validate_on_submit():
        available = AvailableTimes(
            user_id=current_user.id,
            available_start=form.availablefrom.data,
            available_end=form.availableto.data
        )
        db.session.add(available)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('dashboard.html', calendar=cal.formatmonth(2025, 3), form=form, availability=availability, appointments=appointments)

@main.route('/inactive')
@login_required
def inactive():
    if current_user.is_confirmed() == True:
        return redirect(url_for('main.dashboard'))
    return render_template('inactive.html')

@main.route('/resend_confirmation')
@login_required
def resend():
    if current_user.is_confirmed() == True:
        flash('Account already confirmed.')
        return redirect(url_for('main.dashboard'))
    send_validate_account_email(current_user)
    return redirect(url_for('main.inactive'))

@main.route('/myservices', methods=['GET', 'POST'])
@login_required
def myservices():
    servicesList = Service.query.filter_by(user_id=current_user.id).all()
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            user_id=current_user.id,
            is_active=form.is_active.data
            
        )
        db.session.add(service)
        db.session.commit()
        return redirect(url_for('main.myservices'))
    
        # Check if a delete was requested
    if request.method == 'POST' and 'delete_id' in request.form:
        service_id = request.form.get('delete_id')
        service = Service.query.filter_by(id=service_id, user_id=current_user.id).first()
        if service:
            db.session.delete(service)
            db.session.commit()
            flash('Service deleted.', 'success')
        return redirect(url_for('main.myservices'))

    
    return render_template('myservices.html', form=form, servicesList=servicesList)

@main.route('/rewards', methods=['GET', 'POST'])
@login_required
def rewards():
    rewardsList = RewardTransaction.query.filter_by(user_id=current_user.id).all()
    form = RewardsForm()
    if form.validate_on_submit():
        reward = RewardTransaction(
            user_id=current_user.id,
            title=form.title.data,
            points=form.points.data,
            transaction_type=form.service_type.data,
            description=form.description.data
        )
        db.session.add(reward)
        db.session.commit()
        return redirect(url_for('main.rewards'))
    return render_template('rewards.html', form=form, rewardsList=rewardsList)

@main.route('/profilesettings', methods=['GET', 'POST'])
def profilesettings():
    username=current_user.username
    account='Customer'
    if current_user.is_client():
        account='Owner'
    return render_template('profilesettings.html', username=username, account=account)

@main.route('/editprofilesettings', methods=['GET', 'POST'])
def editprofilesettings():
    user = current_user
    account='Customer'
    form = EditForm()
    if form.validate_on_submit():
        user.username=form.username.data
        account=form.account_type.data
        db.session.commit()
        flash('Profile changes saved.')
        return redirect(url_for('main.profilesettings'))

    return render_template('editprofilesettings.html', form=form)

@main.route('/pricing')
@login_required
def pricing():
    form = PriceForm()
    if form.validate_on_submit():
        pricing=form.billing_type.data
        #return redirect(url_for(main.payment))
    return render_template('pricing.html', form=form)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Compose the message
        email_body = f"""
New message from Loyals Contact Form:

Name: {form.name.data}
Email: {form.email.data}

Message:
{form.message.data}
        """
        message = EmailMessage(
            subject="New Contact Form Submission - Loyals",
            body=email_body,
            to=["loyalsbooking@gmail.com"]
        )
        try:
            message.send()
            flash("Thanks for your message! We'll get back to you shortly.")
        except Exception as e:
            print("Email send error:", e)
            flash("Sorry, we couldn't send your message right now.", "danger")

        return redirect(url_for('main.contact'))

    return render_template("contact.html", form=form)