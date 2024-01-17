dex = {}

def pretty_print():
  print()
  for key, value in dex.items():
      print(f"name: {value['name']} | element: {value['element']} | special move: {value['special']} | HP: {value['HP']} | MP: {value['MP']}")
    
while True:
  name = input("Name: ")
  location = input("Element: ")
  weapon = input("Speacial Move: ")
  HP = input("HP: ")
  MP = input("MP: ")
  dex[name] = {"name": name, "element": location, "special":weapon,"HP":HP, "MP":MP }
  quit = input("Again? y/n > ")
  if quit == "n":
    break
pretty_print()