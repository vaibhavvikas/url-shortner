from flask import Blueprint, request
from url_shortner.exception import exception_handler
from url_shortner.service.impl import user_service_impl
from url_shortner.service.impl import url_service_impl
from url_shortner.util import response_util
import url_shortner

bp = Blueprint("user_controller", __name__, url_prefix="/user")


@bp.errorhandler(Exception)
def error_handler(exception):
    return exception_handler \
           .InvalidAPI(exception=exception) \
           .response()


@bp.route("/register", methods={"POST"})
def register_user():
    try:
        json_data = request.get_json()
        userid = json_data["userid"]
        name = json_data["name"]
        if userid in url_shortner.users:
            return response_util.response_to_json("Error! Userid already exists.",
                                                  status="FAILED", status_code=403)
        user = user_service_impl.create_user(userid, name)
        return response_util.response_to_json("User created successfully",
                                              data=user)
    except Exception as e:
        return response_util.error_response(e)


@bp.route("/<path:userid>/shortenurl", methods=["PUT"])
def shorten_url(userid):
    try:
        json_data = request.get_json()
        url = json_data["url"]
        ttl = None
        if "ttl" in json_data:
            ttl = json_data["ttl"]
        data = url_service_impl.encode_url(url, userid, ttl)
        return response_util.response_to_json("URL created successfully",
                                              data=data)
    except Exception as e:
        return response_util.error_response(e)


@bp.route("/<path:userid>/urls", methods=["GET"])
def get_urls(userid):
    try:
        urls = url_service_impl.get_user_urls(userid)
        return response_util.response_to_json(f"URLs retrieved successfully for {userid}!",
                                              data=urls)
    except Exception as e:
        return response_util.error_response(e)
