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
    json_data = request.get_json()
    userid = json_data["userid"]
    name = json_data["name"]
    return user_service_impl.create_user(userid, name)


@bp.route("/<path:userid>/shortenurl", methods=["PUT"])
def shorten_url(userid):
    json_data = request.get_json()
    url = json_data["url"]
    ttl = None
    if "ttl" in json_data:
        ttl = json_data["ttl"]
    return url_service_impl.encode_url(url, userid, ttl)


@bp.route("/<path:userid>/urls", methods=["GET"])
def get_urls(userid):
    return url_service_impl.get_user_urls(userid)
