import random

dictionary = {}

dictionary["Mr. Morgan"] = {"Intelligence": random.randint(0, 99), "Handsomeness": random.randint(0, 99), "L33t c0ding skillz": random.randint(0, 99), "baldness level": random.randint(0, 99)}
dictionary["Mr. Colley"] = {"Intelligence": random.randint(0, 99), "Handsomeness": random.randint(0, 99), "L33t c0ding skillz": random.randint(0, 99), "baldness level": random.randint(0, 99)}

def printer():
    print(f"Mr. Morgan's {stat} level is {dictionary['Mr. Morgan'][stat]}")
    print(f"Mr. Colley's {stat} level is {dictionary['Mr. Colley'][stat]}")
while True:
  print("Top Tumps")
  print("Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")
  card = input("Choose your card: Mr. Morgan or Mr. Colley: ")
  print()
  stat = input("Choose your stat:\n1. Intelligence\n2. Handsomeness\n3. L33t c0ding skillz\n4. Baldness level: ")

  if card != "Mr. Morgan" and card != "Mr. Colley":
      print("Invalid card choice.")
  else:
      printer()
      if dictionary["Mr. Morgan"][stat] > dictionary["Mr. Colley"][stat]:
          print(f"{card} wins!")
      elif dictionary["Mr. Morgan"][stat] < dictionary["Mr. Colley"][stat]:
          other_card = "Mr. Colley" if card == "Mr. Morgan" else "Mr. Morgan"
          print(f"{other_card} wins!")
      else:
          print("It's a tie!")
  again = input("Would you like to play again? (y/n): ")
  if again == "n":
      break