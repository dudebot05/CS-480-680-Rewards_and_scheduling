from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    config[configName].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        db.create_all()

    from .auth import auth as auth_bluprint
    from .routes import main as main_bluprint
    app.register_blueprint(main_bluprint)
    app.register_blueprint(auth_bluprint)

    return app