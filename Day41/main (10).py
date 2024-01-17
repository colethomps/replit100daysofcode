website = {"Name": None,"url": None,"description": None,"stars": None}

for info in website:
  website[info] = input(f"Input the {info} of the website: ")
  print(website[info])
for value, items in website.items():
  print(f"{value}, {items}")