print("Dave's Dodgy Pizzas")

orders = []
while True:
  try:
    f = open("pizzas.txt","r")
    orders = eval(f.read())
    f.close()

  except:
    print("Cannot load pizzas.txt")
  
  pizzas = input("How many pizzas?")
  try:
    pizzas = int(pizzas)
  except:
    print("Please enter a number")
    continue

  size = input("What size?")
  try:
    size = int(size)
  except:
    print("Please enter a number")
    continue

  name = input("Name please")

  print(f"Thanks {name}, you pizzas will cost {pizzas * size}")
  break
  
cost = pizzas * int(size)
order = (name, pizzas, cost)
orders.append(order)

f = open("pizzas.txt", "w")
f.write(str(orders))
f.close()
