from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from .models import db, Service

services = Blueprint('services', __name__)

@services.route('/api/services', methods=['GET'])
def get_services():
    try:
        search = request.args.get('search', '')
        sort = request.args.get('sort', 'name')
        order = request.args.get('order', 'asc')
        
        query = Service.query
        
        if search:
            query = query.filter(Service.name.ilike(f'%{search}%'))
        
        if order == 'asc':
            query = query.order_by(getattr(Service, sort).asc())
        else:
            query = query.order_by(getattr(Service, sort).desc())
            
        services = query.all()
        return jsonify({
            'status': 'success',
            'data': [service.to_dict() for service in services]
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@services.route('/api/services', methods=['POST'])
@login_required
def create_service():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'price']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'status': 'error',
                    'message': f'Missing required field: {field}'
                }), 400
        
        new_service = Service(
            name=data['name'],
            description=data.get('description', ''),
            price=float(data['price']),
            business_owner_id=current_user.id
        )
        
        db.session.add(new_service)
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'data': new_service.to_dict(),
            'message': 'Service created successfully'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500