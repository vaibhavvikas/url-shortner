from flask import Blueprint, request
from url_shortner.exception import exception_handler
from url_shortner.service.impl import user_service_impl
from url_shortner.service.impl import url_service_impl

bp = Blueprint("user_controller", __name__, url_prefix="/user")


@bp.errorhandler(Exception)
def error_handler(exception):
    return exception_handler \
           .InvalidAPI(exception=exception) \
           .response()


@bp.route("/register", methods={"POST"})
def register_user():
    username = request.form["username"]
    userid = request.form["userid"]
    name = request.form["name"]
    return user_service_impl.create_user(userid, username, name)


@bp.route("/<path:userid>/shorten_url", methods=["PUT"])
def shorten_url(userid):
    url = request.form["url"]
    try:
        ttl = request.form["ttl"]
    except:
        ttl = None
    return url_service_impl.encode_url(url, userid, ttl)

