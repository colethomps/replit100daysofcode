print("Life Organizer")
print("")
todo_list = []

def pretty_print():
  print("")
  print("Todo List:")
  for row in todo_list:
    for item in row:
      print("- " + item,end="\t")
  print("")

while True:
  action = input("What would you like to do? a/r/v/q")
  if action[0].strip().lower() == "a":
    item = input("What would you like to add?")
    due = input("When is it due?")
    priority = input("What is the priority?")
    row = [item,due,priority]
    todo_list.append(row)
    print("Added " + item + " to your todo list.")
  elif action[0].strip().lower() == "r":
    remove = input("What would you like to remove?")
    for row in todo_list:
      if remove in row:
        todo_list.remove(row)
    print("Removed " + remove)
  elif action[0].strip().lower() == "v":
    pretty_print()
  elif action[0].strip().lower() == "q":
    break
  else:
    print("Unknown command")