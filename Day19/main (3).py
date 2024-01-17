total = 1000
interestRate = 0.05
interest = 0
for counter in range(10):
  interest = (((total * (1+interestRate)**(counter+1)))-total)
  print("Year", counter,"is $", total+interest)

print("You paid $", interest,"in interest!")