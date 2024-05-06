from flask import Flask
from app.api.v1 import api as api_v1


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api_v1, url_prefix="/api/v1")
