from flask import jsonify


def response_to_json(message, data=None, status="SUCCESS", status_code=200):
    rv = dict()
    rv["message"] = message
    if data: rv["data"] = data
    rv["status"] = status
    response = jsonify(rv)
    response.status_code = status_code
    return response


def error_response(e):
    return response_to_json("Error! " + str(e), \
        status="FAILED", status_code=400)
