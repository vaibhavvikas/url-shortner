from flask import Response
import url_shortner
from url_shortner.service.user_service import User
from url_shortner.util import response_util


def create_user(userid: str, name: str) -> Response:
    try:
        if userid in url_shortner.users:
            return response_util.response_to_json("Error! Userid already exists.",\
                status="FAILED", status_code=403)
        user = User(userid, name)
        url_shortner.users[userid] = user
        print(user)
        return response_util.response_to_json("User created successfully")
    except Exception as e:
        return response_util.error_response(e)
