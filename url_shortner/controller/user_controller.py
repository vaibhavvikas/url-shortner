from flask import Blueprint, request
from url_shortner.exception import exception_handler

bp = Blueprint("url_shortner", __name__, url_prefix="/user")


@bp.errorhandler(Exception)
def error_handler(exception):
    return exception_handler \
           .InvalidAPI(exception=exception) \
           .response()


@bp.route("/register", methods={"POST"})
def register_user():
    user_name = request.form["username"]
    user_id = request.form["userid"]
    name = request.form["name"]
    return "App"
