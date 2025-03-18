class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added ${amount} to the Balance. New balance: ${self.balance}")        

    def transfer_money(self, recipient, amount, entered_pin):
        if entered_pin == self.pin:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                recipient.balance += amount
                print(f"transferred ${amount} to ${recipient.name}")
                return True
            else:
                print("Insufficient funds or invalid amount!")
                return False
        else:
            print("Incorrect pin! Try again loser!")
            return False
            
    def request_money(self, sender, amount, sender_pin, requester_password):
        """Requests money from another user, verifying both PIN and password."""
        if sender.pin == sender_pin:
            if self.password == requester_password:
                if 0 < amount <= sender.balance:
                    sender.balance -= amount
                    self.balance += amount
                    print(f"Request successful! ${amount} received from {sender.name}.")
                    return True
                else:
                    print("Sender has insufficient funds.")
                    return False
            else:
                print("Incorrect password. Request failed.")
                return False
        else:
            print("Incorrect sender PIN. Request failed.")
            return False
    """ Driver Code for Task 1 """
# user1 = User("Mann", 786619, "password")
# print(user1.name)
# print(user1.pin)
# print(user1.password)

    """ Driver Code for Task 2 """
# user = User("Mann", 786619, "password")
# print(user.name, user.pin, user.password)
# user.change_name("MannJaiswal")
# user.change_pin(788888)
# user.change_password("password123")
# print(user.name, user.pin, user.password)

    """ Driver Code for Task 3"""
# bank_user = BankUser("Natasha", 128436, "BlackWidow")
# print(bank_user.name, bank_user.pin, bank_user.password, 
#       bank_user.balance)

    """ Driver Code for Task 4"""
# bank_user = BankUser("Natasha", 128436, "BlackWidow")
# print(bank_user.name, bank_user.pin, bank_user.password)
# bank_user.show_balance()
# bank_user.deposit(200)
# bank_user.withdraw(20)
# bank_user.show_balance()

    """ Driver Code for Task 5"""
bank_user = BankUser("Natasha", 128436, "BlackWidow")
print(bank_user.name, bank_user.pin, bank_user.password)
bank_user2 = BankUser("TChalla", 786619, "BlackPanther")
print(bank_user2.name, bank_user2.pin, bank_user2.password)
bank_user2.deposit(5000)
bank_user2.show_balance()
bank_user.show_balance()
success = bank_user2.transfer_money(bank_user, 500, 786619)
bank_user.show_balance()
bank_user2.show_balance()
if success:
    bank_user2.request_money(bank_user, 100, 128436, "BlackPanther")
bank_user.show_balance()
bank_user2.show_balance()


