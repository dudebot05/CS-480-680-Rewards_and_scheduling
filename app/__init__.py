from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mailman import Mail

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    from .auth import auth as auth_bluprint
    from .routes import main as main_bluprint
    app.register_blueprint(main_bluprint)
    app.register_blueprint(auth_bluprint)

    return app