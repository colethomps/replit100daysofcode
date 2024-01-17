print("To Do List Manager")
toDo = []

def addTask():
  for task in toDo:
    print(task,"\n")

while True:
  action = input("What would you like to do? (add, edit, view) ")
  if action == "add":
    task = input("What task would you like to add? ")
    toDo.append(task)
  elif action == "edit":
    task = input("What task?")
    if task in toDo:
      toDo.remove(task)
    else:
      print("That task is not in the toDo")
  addTask()
    