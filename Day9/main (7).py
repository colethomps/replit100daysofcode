year = int(input("What year were you born?"))
if year < 1925:
  print("I don't know your Generation Name")
elif year <= 1946:
  print("Traditionalist")
elif year <= 1964:
  print("Baby Boomers")
elif year <= 1981:
  print("Generation X")
elif year <= 1995:
  print("Millenials")
elif year <= 2015:
  print("Generation Z")
else:
  print("You're just a kid")