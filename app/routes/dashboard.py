from functools import wraps

from app.models import db
from app.static.edit import EditForm
from app.static.pricing import PriceForm
from . import main
from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..auth.routes import send_validate_account_email
import calendar

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
    return render_template('dashboard.html', calendar=cal.formatmonth(2025, 3))

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
def myservices():
    return render_template('myservices.html')

@main.route('/rewards')
@login_required
def rewards():
    return render_template('rewards.html')

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
def pricing():
    form = PriceForm()
    if form.validate_on_submit():
        pricing=form.billing_type.data
        #return redirect(url_for(main.payment))
    return render_template('pricing.html', form=form)

@main.route('/')
def index():
    return render_template('index.html')