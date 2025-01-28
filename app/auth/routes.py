from ensurepip import bootstrap
from flask import render_template, redirect, request, url_for, flash
#from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..static.login import LoginForm
from ..static.register import RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    #logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@auth.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')
