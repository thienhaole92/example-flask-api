from flask import Response
from . import api


@api.route("/get-success")
def get_success():
    return Response("Get Success", status=200)
