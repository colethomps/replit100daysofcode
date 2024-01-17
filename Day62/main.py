import datetime, os, time
from replit import db

diary = []

def add_entry(entry):
  now = datetime.datetime.today()
  db[now] = entry
def view_diary(diary):
  keys = db.keys()
  for key in keys:
    print(key, db[key])
    option = input("Next or Exit?")
    os.system("clear")
    if option == "Exit":
      break
    else:
      continue
while True:
  password = db["password"]
  tried_password = input("Enter your password: ")
  if tried_password == password:
    print("Welcome back!")
    break
  else:
    print("Wrong password!")
  
os.system("clear")
while True:
  print("Welcome to the Diary App!")
  print("What would you like to do?")
  print("1. Add an entry")
  print("2. View diary")
  str_input = str(input(" > "))
  os.system("clear")
  if str_input == "1":
    str_entry = input("What do you want to say?")
    add_entry(str_entry)
    os.system("clear")
  elif str_input == "2":
    view_diary(diary)
    print("No more, exiting...")
    time.sleep(3)
    os.system("clear")
