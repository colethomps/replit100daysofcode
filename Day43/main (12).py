import random

list = []
for i in range(9):
    list.append(random.randint(1, 90))
list.sort()

card = [[0,0,0],[0,"Bingo",0],[0,0,0]]
for i in range(9):
  if card[i//3][i%3] == "Bingo":
    card[i//3][i%3] == "Bingo"
    i-1
  else:
    card[i//3][i%3] = list[i]
print("Cole Thompson's Bingo Card Generator")
print(f"{card[0][0]}|{card[0][1]}|{card[0][2]}|\n{card[1][0]}|{card[1][1]}|{card[1][2]}|\n{card[2][0]}|{card[2][1]}|{card[2][2]}|")
