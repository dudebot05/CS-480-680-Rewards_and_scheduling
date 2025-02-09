from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import booking
    app.register_blueprint(booking.bp)

    return app