myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = float(input("What was the tip %?"))
tip = 1 + (tip/100)
answer = (myBill * tip)/ numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)