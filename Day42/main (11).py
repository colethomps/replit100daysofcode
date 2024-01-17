
mokebeast = {"name": None, "type":None, "move":None,"HP":None,"MP":None}

print("MokeBeast - The non-copyright Genric Beast Battle Game")
for info in mokebeast:
    mokebeast[info] = input(f"Input your beast's {info}: ")

def output():
  print(f"Your beast is called {mokebeast['name']}. It is a {mokebeast['type']} type with a special move of {mokebeast['move']}")

if mokebeast["type"].lower() == "earth":
  print("\033[0;32m")
  output()
elif mokebeast["type"].lower() == "wind":
  print("\033[0;37m")
  output()
elif mokebeast["type"].lower() == "fire":
  print("\033[0;31m")
  output()
else:
  output()