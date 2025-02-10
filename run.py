import os
from flask import Flask
from config import config
from app import create_app, db
from app.models.rewards import RewardTransaction
from app.models.booking import Booking
from app.models.role import Role
from app.models.user import User
from waitress import serve
from app.routes import main as main_blueprint  # Changed to match routes/__init__.py

app = create_app(os.getenv('FLASK_CONFIG'))
app.register_blueprint(main_blueprint)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Booking=Booking, RewardTransaction=RewardTransaction)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))