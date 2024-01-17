import random
def hp():
  value = (random.randint(1,6))*(random.randint(1,8))
  return value


print("Character Stats Generator")
while True:
  HPvalue = hp()
  input("Name your warrior:")
  print("Their HP is:",HPvalue)
  exit = input("Type 'exit' to Exit")
  if exit == "exit":
    break
  else:
    continue