class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password

user1 = User("Mann", "mannjaiswal5@gmail.com", "password123")
print(user1.username, user1.email, user1.password)

user1.change_password("bestpassword")
print(user1.password)