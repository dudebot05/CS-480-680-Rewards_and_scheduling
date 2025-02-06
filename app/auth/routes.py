from ensurepip import bootstrap
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .login_manager import load_user
from .. import db, login_manager
from ..models.user import User
from ..static.login import LoginForm
from ..static.register import RegistrationForm
#Added by Iyona
from ..static.forgotpass import ForgotPassForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.dashboard')
            return redirect(next)
        flash('Invalid Username or Password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Account created')
        flash('You can now login')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('auth/admin.html')

#Added by Iyona
@auth.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpass():
    form = ForgotPassForm()
    user = User(
        email=form.email.data,
        )
    flash('Account created')
    flash('You can now login')
    return render_template('auth/forgotpass.html', form=form)