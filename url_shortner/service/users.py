class User:

    def __init__ (self, identity, user_id, name):
        self.identity = identity
        self.user_id = user_id
        self.name = name
        self.urls = {}
        self.status = True
    
    def __str__(self):
        return f"IDENTITY: {self.identity} \nUSERNAME: {self.user_id} \
            STATUS: {'Account is Active!' if self.status else 'Deactivated Account!'}"
