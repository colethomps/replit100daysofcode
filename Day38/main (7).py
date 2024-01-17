sentence = input("What sentence do you want rainbow-ising?")
for i in sentence:
  if i == 'r':
    print(f"\033[0;31m{i}", end="")
  elif i == 'b':
    print(f"\033[0;34m{i}", end="")
  elif i == 'g':
    print(f"\033[0;32m{i}", end="")
  elif i == 'p':
    print(f"\033[0;35m{i}", end="")
  elif i == 'y':
    print(f"\033[1;33m{i}", end="")
  else:
    print(i, end="")