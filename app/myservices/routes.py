from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from .models import db, Service
from .forms import ServiceForm

myservices = Blueprint('myservices', __name__)

@myservices.route('/api/myservices', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify({'services': [service.to_dict() for service in services]})

@myservices.route('/api/myservices/create', methods=['GET', 'POST'])
@login_required
def create_service():
    form = ServiceForm()
    if form.validate_on_submit():
        new_service = Service(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            is_active=form.is_active.data,
            business_owner_id=current_user.id
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify({'status': 'success', 'message': 'Service created'})
    return render_template('myservices/create.html', form=form)