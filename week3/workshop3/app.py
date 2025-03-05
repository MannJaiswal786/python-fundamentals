from donations_pkg.homepage import show_homepage
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
    print("TODO: Write Login Functionality")
 elif option == 2:
    print("TODO: Write Register Functionality")
 elif option == 3:
    print("TODO: Write Donate Functionality")
 elif option == 4:
    print("TODO: Show Donations")
 elif option == 5:
    print("Exiting the program. Goodbye!!!")
    break
 else:
    print("Invalid option. Please choose an option between 1 and 5")

