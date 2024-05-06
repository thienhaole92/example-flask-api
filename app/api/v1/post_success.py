from flask import request, jsonify
from . import api


@api.route("/post-success", methods=["POST"])
def post_success():
    payload = request.get_json()

    if payload.get("say_hello") is True:
        output = jsonify({"message": "Hello!"})
    else:
        output = jsonify({"message": "..."})

    return output
