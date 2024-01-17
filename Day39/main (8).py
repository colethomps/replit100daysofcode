import random
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
guessed = ""
word = random.choice(listOfWords)
counter = 0
failcounter = 0
print("My word is:")
for i in range(len(word)):
  print("_", end = "")
print()

while True:
  guess = input("Guess a letter:").strip().lower()
  for i in range(len(word)):
    if guess in word[i]:
      guessed += guess
      print(word[i],end="")
    elif word[i] in guessed:
      print(word[i],end="")
    else:
      print("_",end="")
  
  if guess in word.lower():
    print("\nCorrect!")
  else:
    failcounter += 1
    print("\nIncorrect")
  counter +=1
  if failcounter > 4:
    print("You lost!")
    break
  if sorted(guessed) == sorted(word):
    print(f"It took you {counter} guesses to guess {word}")
    break

  
  
