from ensurepip import bootstrap
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..static.login import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')

@auth.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template('auth/admin.html')
