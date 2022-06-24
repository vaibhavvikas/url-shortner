class User:

    def __init__ (self, userid, username, name):
        self.userid = userid
        self.username = username
        self.name = name
        self.status = True
        self.urls = {}

    def deactivate_account(self):
        self.status = None
            
    def __str__(self):
        return (
            f"userid: {self.userid}\n"
            f"username: {self.username}\n"
            f"status: {'Account is Active!' if self.status else 'Deactivated Account!'}"
        )