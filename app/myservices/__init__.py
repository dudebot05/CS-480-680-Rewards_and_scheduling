from flask import Flask
from .models import db
from .routes import myservices

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salon.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    db.init_app(app)
    app.register_blueprint(myservices)
    
    with app.app_context():
        db.create_all()
    
    return app