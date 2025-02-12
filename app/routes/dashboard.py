from functools import wraps
from . import main
from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..auth.routes import send_validate_account_email

def check_is_confirmed(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_confirmed is False:
            flash("Please confirm your account!", "warning")
            return redirect(url_for("main.inactive"))
        return func(*args, **kwargs)

    return decorated_function

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
@check_is_confirmed
def dashboard():
    return render_template('dashboard.html')

@main.route('/inactive_accounts')
@login_required
def inactive():
    if current_user.is_confirmed:
        return redirect(url_for('main.dashboard'))
    return render_template('inactive.html')

@main.route('/resend_confirmation')
@login_required
def resend():
    if current_user.is_confirmed:
        flash('Account already confirmed.')
        return redirect(url_for('main.dashboard'))
    send_validate_account_email(current_user)
    return redirect(url_for('main.inactive'))

@main.route('/')
def index():
    return redirect(url_for('auth.login'))