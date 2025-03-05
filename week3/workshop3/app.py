from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
 show_homepage()

 if authorized_user == "":
    print("You must be logged in to donate")
 else:
    print(f"Logged in as: {authorized_user}")

 try:
  option = int(input("Choose an option: "))
 except ValueError:
    print("Invaliid input. Please enter a number between 1 and 5.")
    continue

 if option == 1:
   username = input("Enter username: ")
   password = input("Enter password: ")
   authorized_user = login(database, username, password)
 elif option == 2:
   username = input("Username: ")
   password = input("Password: ")
   authorized_user = register(database, username)
   if authorized_user != "":
      database[authorized_user] = password
 elif option == 3:
   if authorized_user == "":
      print("You are not logged in")
   else: 
     donation_string = donate(authorized_user)
     donations.append(donation_string)
 elif option == 4:
   show_donations(donations)
 elif option == 5:
    print("Exiting the program. Goodbye!!!")
    break
 else:
    print("Invalid option. Please choose an option between 1 and 5")

