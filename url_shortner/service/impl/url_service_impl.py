from url_shortner.service.url_service import URL
from datetime import datetime
import url_shortner
import random


def string_encode() -> str:
    flag = random.randint(0, 1)
    return chr(random.randint(65, 90)*flag + random.randint(97, 122)*(1-flag))


def url_encoder(url: str) -> str:
    return "".join([string_encode() for _ in range(10)])


def encode_url(url: str, user=None, ttl=None) -> dict:
    if user:
        encoded_url = URL(url, user, ttl)
        url_shortner.users[user].urls[encoded_url.shortened_url] = encoded_url
    else:
        encoded_url = URL(url, ttl=60)
    url_shortner.urls[encoded_url.shortened_url] = encoded_url
    return encoded_url.__dict__


def get_all_urls() -> dict:
    data = {}
    for each in url_shortner.urls:
        data[each] = url_shortner.urls[each].__dict__
    return data


def get_user_urls(userid: str) -> dict:
    data = {}
    for each in url_shortner.users[userid].urls:
        data[each] = url_shortner.users[userid].urls[each].__dict__
    return data


def is_expired(url: URL) -> bool:
    if not url.ttl:
        return False
    return int(datetime.now().strftime("%d%m%y%H%M%S")) > \
        int(url.creation_time) + url.ttl*60


def get_original_url(url: str) -> dict:
    url_object = url_shortner.urls[url]
    if is_expired(url_object):
        if url_object.owner:
            url_shortner.users[url_object.owner].urls.pop(url)
        url_shortner.urls.pop(url)
        return "Sorry! URL Expired."
    return url_shortner.urls[url].__dict__
