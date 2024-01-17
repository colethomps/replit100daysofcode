from replit import db
import random
keys = db.keys()

user = input("Username >")
ans = input("Password >")

if user in keys:
  if db[user]["password"] == hash(ans+db[user]["salt"]):
    print("Logged in!")
  else:
    print("Wrong Pass")
  
else:
  salt = random.randint(1000, 9999)
  newpass = ans + str(salt)
  db[user] = {'password': hash(newpass), 'salt': str(salt)}
  print("User established")



