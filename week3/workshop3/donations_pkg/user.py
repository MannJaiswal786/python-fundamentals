def login(database, username, password):
 if username in database:
    if database[username] == password:
      print(f"Welcome back, {username}")
      return username
    else:
      print("Incorrect password. Please try again")
      return ""
 else:
   print("Username not found. Please register first")
   return ""
 
def register(database, username):
  if username in database:
    print("Username already registered")
    return ""
  else:
    print(f"username {username} has been registered")
    return username
  

