from flask import Blueprint

api = Blueprint("api_v1", __name__)

from . import get_success, post_success
