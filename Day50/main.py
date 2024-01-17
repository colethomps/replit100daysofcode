import random
print("Idea Storage")
print("------------")
choice = ''


while choice != 'exit':
  choice = input("What do you want to do? (add, list, exit): ")
  if choice == 'add':
    f = open("my.ideas", "a+")
    add = input("What is the idea? ")
    f.write(add+"\n")
    f.close()
  elif choice == 'list':
    f = open("my.ideas", "r")
    ideas = f.readlines()
    if len(ideas) == 0:
      print("No ideas found.")
    else:
      random_index = random.randint(0, len(ideas) - 1)
      print(f"Random Idea: {ideas[random_index].strip()}")
