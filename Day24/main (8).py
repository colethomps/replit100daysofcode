import random
def dice(sides):  
 print(random.randint(1, sides))

print("Infinity Dice")
while True:
  userSides = int(input("How many sides?"))
  dice(userSides)
  again = input("Roll again? (y/n)")
  if again == "n":
    break
  else:
    continue