print("HIGH SCORE TABLE")

f = open("savedFile.txt", "a+")
breaker = 'y'
while breaker !='n':
  inputer = input("Enter your initials: ")
  score = input("Enter your score: ")
  f.write(inputer +" "+ score + "\n")
  breaker = input("Do you want to add another score? (y/n)")

f.close()