f = open("high.score","r")
print("Current Leader")
print("")
print("Analyzing high scores...")
print()

contents = f.read()
contents = contents.split() #added split here
max = 0
for i in range(len(contents)):
  if i%2 == 1:
    contents[i] = int(contents[i])
    if max < int(contents[i]):
      name = contents[i-1]
      max = contents[i]
print("Highest score: ",name, max)
