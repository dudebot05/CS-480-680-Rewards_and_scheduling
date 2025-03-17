from functools import wraps

from .. import db
from app.models.rewards import RewardTransaction
from app.static.edit import EditForm
from app.static.rewards import RewardsForm
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

@main.route('/')
def index():
    return redirect(url_for('auth.login'))