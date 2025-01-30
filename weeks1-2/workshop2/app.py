from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("    === Automated Teller Machine ===    ")
name = input("Enter your name to register: ")
pin = input("Enter PIN: ")
balance = 0

if (len(name) > 1 and len(name) <= 10 ):
 print(name + " has been registered with a balance of: " + str(balance))
else:
  print("Name should be between 1 and 10 characters")


print("LOGIN")
while True:
  name_to_validate = input("Enter Name: ")
  pin_to_validate = input("Enter Pin: ")
  if(name_to_validate == name and pin_to_validate == pin):
    print("Login Successful")
    break
  else:
     print("Invalid Credentials")
    
while True:
   atm_menu(name)
   option = input("Choose an option: ")
   if(option == "1"):
      account.show_balance(balance)
   elif (option == "2"):
    balance = account.deposit(balance)
    print(balance)
   elif (option == "3"):
    balance = account.withdraw(balance)
    print (balance)
   elif(option == "4"):
     account.logout(name) 
     break
