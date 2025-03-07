class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password

class BankUser(User):
    def __init__(self,username,email, password):
        super().__init__(username, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.username, "Has a balance of:",self.balance)

bankuser1 = BankUser("Mann", "mannjaiswal5@gmail.com", "bestPassword")
