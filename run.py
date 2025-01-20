import os
from flask import Flask
from config import config
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG'))

if __name__ == '__main__':
    app.run()