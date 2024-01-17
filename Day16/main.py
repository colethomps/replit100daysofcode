print("Fill in the Blank Lyrics!")
count = 1
while True:
  lyrics = input("Never going to ____ you up! ")
  if lyrics == "give":
    break
  else:
    print("Nope! Try Again")
  count += 1
print("Well Done! It only took you", count , "attempts.")