import os
from flask import Flask
from config import config

app = create_app(os.getenv('FLASK_CONFIG'))

if __name__ == '__main__':
    app.run()