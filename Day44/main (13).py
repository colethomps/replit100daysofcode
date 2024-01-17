import random,os

def pretty_print():
  print()
  for row in card:
    for item in row:
      print(f"{item: ^6} |",end="\t")
    print()
  print()

list = []
for i in range(8):
    list.append(random.randint(1, 90))
list.sort()

card = [['X','X','X'],['X',"Bingo",'X'],['X','X','X']]
number = -1
while True:
  if number in list:
    for i in range(8):
      if list[i] == number:
          if i >= 4:
            card[(i+1)//3][(i+1)%3] = number
          else: 
            card[i//3][i%3] = number
  
  print("Cole Thompson's Bingo Card Generator")
  pretty_print()
  print(list)
  breaker = 'Yes'
  for i in range(9):
    if card[i//3][i%3] == "X":
      breaker = 'No'
  if breaker == 'Yes':
    print("You Win!")
    break
  number = int(input("Next number: "))
  os.system("clear")

  