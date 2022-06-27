from flask import Blueprint, request
from url_shortner.service.impl import url_service_impl
from url_shortner.util import response_util

bp = Blueprint("url_controller", __name__, url_prefix="/url")


@bp.route("/listurls", methods=["GET"])
def get_all_urls():
    try:
        urls = url_service_impl.get_all_urls()
        return response_util.response_to_json("URLs retrieved successfully",
                                              data=urls)
    except Exception as e:
        return response_util.error_response(e)


@bp.route("/shortenurl", methods=["PUT"])
def shorten_url():
    try:
        original_url = request.get_json()["url"]
        shortened_url = url_service_impl.encode_url(original_url)
        return response_util.response_to_json("URL created successfully",
                                              data=shortened_url)
    except Exception as e:
        return response_util.error_response(e)


@bp.route("/geturl/<path:url>", methods=["GET"])
def decode_url(url):
    try:
        url_info = url_service_impl.get_original_url(url)
        return response_util.response_to_json("URL retrieved successfully",
                                              data=url_info)
    except Exception as e:
        return response_util.error_response(e)
