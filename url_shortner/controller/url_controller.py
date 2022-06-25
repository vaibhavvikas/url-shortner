from flask import Blueprint, request
from url_shortner.service.impl import url_service_impl

bp = Blueprint("url_controller", __name__, url_prefix="/url")


@bp.route("/listurls", methods=["GET"])
def get_all_urls():
    return url_service_impl.get_all_urls()


@bp.route("/shortenurl", methods=["PUT"])
def shorten_url():
    url = request.get_json()["url"]
    return url_service_impl.encode_url(url)


@bp.route("/geturl/<path:url>", methods=["GET"])
def decode_url(url):
    return url_service_impl.get_original_url(url)
