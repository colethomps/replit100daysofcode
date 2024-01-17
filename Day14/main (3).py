from getpass import getpass as input

print("Epic Rock, Paper, Sissors Battle!")
print("Select your move (R,P,S")


player1 = input("Player 1: ")
player2 = input("Player 2: ")

if player1 == "R" and player2 == "S":
  print("Player1's Rock beats Player2's Sissors ")
elif player1 == "R" and player2 == "P":
  print("Player1's Rock loses to Player2's Paper")
elif player1 == "R" and player2 == "R":
  print("Both choose rock, Tie!")
elif player1 == "P" and player2 == "P":
  print("Both choose paper, Tie!")
elif player1 == "P" and player2 == "R":
  print("Player1's Paper beats Player2's Rock ")
elif player1 == "P" and player2 == "S":
  print("Player1's Paper loses to Player2's Sissors")
elif player1 == "S" and player2 == "S":
  print("Both choose Sissors, Tie!")
elif player1 == "S" and player2 == "P":
  print("Player1's Sissors beats Player2's Paper ")
elif player1 == "S" and player2 == "R":
  print("Player1's Sissors loses to Player2's Rock")
else:
  print("You messed it up... fail")