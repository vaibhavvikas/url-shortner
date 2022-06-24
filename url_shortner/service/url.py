from datetime import datetime


class URL:

    def __init__(self, url, ttl=None):
        self.url = url
        self.creation_time = datetime.now().strftime("%d%m%y%H%M%S")
        self.ttl = ttl

    def __str__(self):
        return "URL is {self.url}. It was created on {self.creation_time}."
