class User:

    def __init__(self, userid, name):
        self.userid = userid
        self.name = name
        self.status = True
        self.urls = {}

    def deactivate_account(self):
        self.status = None

    def __str__(self):
        return (
            f"userid: {self.userid}\n"
            f"status: {'Account is Active!' if self.status else 'Deactivated Account!'}"
        )
