from flask import Response
from url_shortner.service.url_service import URL
from url_shortner.util import response_util
from datetime import datetime
import url_shortner
import random


def string_encode() -> str:
    flag = random.randint(0,1)
    return chr(random.randint(65, 90)*flag + random.randint(97, 122)*(1-flag))


def url_encoder(url: str) -> str:
    return "".join([string_encode() for _ in range(max(10, len(url)))])


def encode_url(url: str, user=None, ttl=None) -> Response:
    try:
        if user:
            encoded_url = URL(url, user, ttl)
            print(url_shortner.users)
            url_shortner.users[user].urls[encoded_url.shortened_url] = encoded_url
        else:
            encoded_url = URL(url, ttl=60)
        url_shortner.urls[encoded_url.shortened_url] = encoded_url
        return response_util.response_to_json("URL created successfully", data=encoded_url.__dict__)
    except Exception as e:
        return response_util.error_response(e)


def get_all_urls() -> Response:
    try:
        data = {}
        print(url_shortner.urls)
        for each in url_shortner.urls:
            data[each] = url_shortner.urls[each].__dict__
        return response_util.response_to_json("URLs retrieved successfully", data=data)
    except Exception as e:
        return response_util.error_response(e)


def get_user_urls(userid: str) -> Response:
    try:
        data = {}
        for each in url_shortner.users[userid].urls:
            data[each] = url_shortner.users[userid].urls[each].__dict__
        print(data)
        return response_util.response_to_json(f"URLs retrieved successfully for {userid}!",\
            data=data)
    except Exception as e:
        return response_util.error_response(e)


def is_expired(url: URL) -> bool:
    if not url.ttl:
        return False
    return int(datetime.now().strftime("%d%m%y%H%M%S")) > int(url.creation_time) + url.ttl*60


def get_original_url(url: str) -> Response:
    try:
        url_object = url_shortner.urls[url]
        if is_expired(url_object):
            if url_object.owner:
                url_shortner.users[url_object.owner].urls.pop(url)
            url_shortner.urls.pop(url)
            return "Sorry! URL Expired."
        data = url_shortner.urls[url].__dict__
        return response_util.response_to_json("URLs retrieved successfully", data=data)
    except Exception as e:
        return response_util.error_response(e)
