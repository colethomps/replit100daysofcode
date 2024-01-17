names = []
while True:
  firstName = str(input("First Name:").strip().capitalize())
  lastName = str(input("Last Name:").strip().capitalize())
  if (firstName + " " + lastName) in names:
    print("Name already exists.")
  else:
    names.append(firstName + " " + lastName)
  print(names)