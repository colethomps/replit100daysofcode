import time, os, random

todoList = []

folderPath = "todo/"

if os.path.exists(folderPath):
  print("Auto save folder exists.")
else:
  os.mkdir(folderPath)

filename = (folderPath + "todo" +str(random.randint(0, 100000000)) + ".txt")



f=open("todoList.txt","r")
todoList = eval(f.read())
f.close()

print("To Do List Manager")
print()

def printerList():
  os.system("clear")
  print("List:")
  for item in range(len(todoList)):
    print(f"{item}:  {todoList[item]}")
    time.sleep(.25)

while True:
  os.system("clear")
  choice = input("Do you want to view, add, edit,remove an item from your list?")
  if choice == "view":
    printerList()
  elif choice == "add":
    item = input("What item do you want to add?")
    if item not in todoList:
      todoList.append(item)
  elif choice == "edit":
    item = input("What item do you want to edit?")
    for i in range(len(todoList)):
      if todoList[i] == item:
        todoList[i] = input("what would you like to change it to?")
        print("done.")
      else:
        print("That item is not in the list")
  elif choice == "remove":
    item = input("What item do you want to remove?")
    sure = input("Are you sure you want to remove this item?")
    if sure.lower() == "yes":
      todoList.remove(item)
      print("Done.")
    else:
      print("Not removed.")
  else:
    print("That is not an option")
  time.sleep(1)
  
  f = open(filename, "w")
  f.write(str(todoList))
  f.close()

  
  f = open("todoList.txt", "w")
  f.write(str(todoList))
  f.close()