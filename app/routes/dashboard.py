from . import main
from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/')
def index():
    return redirect(url_for('auth.login'))