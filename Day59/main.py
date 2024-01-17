print("Palindrom Checker")

word = input("Input a word > ").lower()
reversed_string = word[::-1].lower()
counter = 0


for i in range(len(word)):
    if word[i] == reversed_string[i]:
      continue
    else:
      counter =1
if counter >= 1:
  print("This word is not a palindrom")
else:
  print("This word is a palindrom")