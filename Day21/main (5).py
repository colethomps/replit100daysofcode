print("Math Game!")

multiples = int(input("Name your multiples:"))
guess = 0
score = 0
for i in range(1,11):
  print(i,"x",multiples,"=")
  guess = int(input(""))
  if guess == i*multiples:
    score += 1
    print("Correct!")
  else:
    print("Incorrect, the answer is", i*multiples)

if score ==10:
  print("Perfect score! 100%")
else:
  print("Your final score is", score,"/10")
  