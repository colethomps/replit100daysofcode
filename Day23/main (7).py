def loginInput():
  print("Replit Login System")
  while True:
    username = input("What is your username:")
    password = input("What is your password:")
    if username == "admin" and password == "password":
      print("Welcome to Replit!")
      break
    else:
      print("Whoops! I don't recognise that username or password, try again")
      
  
loginInput()