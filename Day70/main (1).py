import os

normal = os.environ['normal'] 
admin = os.environ['admin'] 

userPass = input("Password > ")

if userPass == normal:
  print("Hello Normie")
elif userPass == admin:
  print("Hello Admin")
else:
  print("Better luck next time")