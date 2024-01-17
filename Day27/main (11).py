import random, time, os
def hp():
  hp = (((random.randint(1,6))*(random.randint(1,12)))/2)+10
  return hp

def strength():
  strength = (((random.randint(1,6))*(random.randint(1,12)))/2)+12
  return strength

def character():
  time.sleep(.5)
  name = input("Name Your Legend:")
  time.sleep(.5)
  os.system("clear")
  type = input("Character Type:")
  time.sleep(.5)
  os.system("clear")
  print(name,"the", type)
  print("Health:",hp())
  print("Strength:",strength())
  return name, type, hp

while True:
  print("Character Builder")
  character()
  time.sleep(5)
  os.system("clear")
  exit = input("May your name go down in Legend...(Press 'r' to redo')")
  if exit == 'r':
    os.system("clear")
    continue
  else:
    break

  