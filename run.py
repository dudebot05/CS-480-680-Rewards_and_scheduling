import os
from flask import Flask
from config import config
from app import create_app, db
from app.models.rewards import RewardTransaction
from app.models.booking import Booking
from app.models.role import Role
from app.models.user import User

app = create_app(os.getenv('FLASK_CONFIG'))

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Booking=Booking, RewardTransaction=RewardTransaction)

with app.app_context():
    Role.insert_roles()

if __name__ == '__main__':
    app.run()
