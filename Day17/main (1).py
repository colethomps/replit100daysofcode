from getpass import getpass as input

print("Epic Rock, Paper, Sissors Battle!")
print("Select your move (R,P,S")



player1score = 0
player2score = 0

while True:
  player1 = input("Player 1: ")
  player2 = input("Player 2: ")
  if player1 == "R" and player2 == "S":
    print("Player1's Rock beats Player2's Sissors ")
    player1score +=1
  elif player1 == "R" and player2 == "P":
    print("Player1's Rock loses to Player2's Paper")
    player2score +=1
  elif player1 == "R" and player2 == "R":
    print("Both choose rock, Tie!")
  elif player1 == "P" and player2 == "P":
    print("Both choose paper, Tie!")
  elif player1 == "P" and player2 == "R":
    print("Player1's Paper beats Player2's Rock ")
    player1score +=1
  elif player1 == "P" and player2 == "S":
    print("Player1's Paper loses to Player2's Sissors")
    player2score +=1
  elif player1 == "S" and player2 == "S":
    print("Both choose Sissors, Tie!")
  elif player1 == "S" and player2 == "P":
    print("Player1's Sissors beats Player2's Paper ")
    player1score +=1
  elif player1 == "S" and player2 == "R":
    print("Player1's Sissors loses to Player2's Rock")
    player2score +=1
  else:
    print("You messed it up... fail")
  if player1score < 3 and player2score < 3:
    print("Player1's score: ", player1score)
    print("Player2's score: ", player2score)
    continue
  else:
    break 
if player1score == 3:
    print("Player 1 Wins!")
elif player2score == 3:
    print("Player 2 Wins!")