class User:
    def __init__(self, username):
        self.username = username


class AuthenticatedUser(User):
    def login(self, password):
        return password == "secret"


user = AuthenticatedUser("admin")
print(user.login("secret"))
