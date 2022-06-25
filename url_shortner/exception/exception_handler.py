from flask import jsonify


class InvalidAPI(Exception):
    status_code = 400
    status = "FAILED"

    def __init__(self, exception, status_code=None, payload=None):
        super().__init__()
        self.message = str(exception)
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def response(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        rv["status"] = self.status
        res = jsonify(rv)
        res.status_code = self.status_code
        return res
