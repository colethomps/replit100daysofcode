import time, os

todoList = []

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
    if sure == "yes":
      todoList.remove(item)
      print("Done.")
    else:
      print("Not removed.")
  else:
    print("That is not an option")
  time.sleep(1)
  