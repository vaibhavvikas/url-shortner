import url_shortner
from url_shortner.service.user_service import User


def create_user(userid: str, name: str) -> dict:
    user = User(userid, name)
    url_shortner.users[userid] = user
    return user.__dict__
