import random

print("One-Million to One")
counterGuess=0
number = random.randint(1,1000000)
while True:
  guess = int(input("What is your guess? "))
  counterGuess += 1
  if guess == number:
    print("Correct!")
    print()
    print("It took you",counterGuess, "guesses to get it right.")
    break
  elif guess < 0:
    print("Exiting program...")
    break
  elif guess > number:
    print("Too high!")
  elif guess < number:
    print("Too low!")
  elif guess == 'exit':
    break
  continue