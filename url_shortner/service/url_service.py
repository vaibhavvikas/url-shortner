from datetime import datetime
from url_shortner.service.impl import url_service_impl

class URL:

    def __init__(self, url, owner=None, ttl=None):
        self.url = url
        self.shortened_url = url_service_impl.url_encoder(url)
        self.creation_time = datetime.now().strftime("%d%m%y%H%M%S")
        self.owner = owner
        self.ttl = ttl

    def __str__(self):
        return (
            f"url: {self.url}\n"
            f"shortened_url: {self.shortened_url}\n"
            f"creation_time: {self.creation_time}\n"
            f"Expiry: {str(self.ttl)+' minutes' if self.ttl else 'Never'}"
        )
