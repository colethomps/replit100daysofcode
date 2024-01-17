import datetime, os, time, random
from replit import db

keys = db.keys()

while True:
  usern = input("Username > ")
  passw = input("Password > ")
  if usern in keys:
    if db[usern]['password'] == passw:
      print("Logged in!")
      time.sleep(1)
      break
    else:
      print("Wrong pass")
  else: 
    db[usern] = {'password': passw, 'salt': str(random.randint(1000,9999))}
    print("New Account Created")
    break
os.system("clear")

def add_entry(str_entry):
  now = datetime.datetime.today()
  db[usern] = {f'{now}': f"{str_entry}"}
def view_diary():
  for key in db[usern]:
      if key == 'password':
        continue
      if key == 'salt':
        continue
      print(key + ": " + db[usern][key])
      option = input("Next or Exit?")
      os.system("clear")
      if option.lower() == "Exit":
        break
      else:
        continue


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
    view_diary()
    print("No more, exiting...")
    time.sleep(3)
    os.system("clear")
