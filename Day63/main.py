## test.py file ##############
import random
import test as tt

num = random.randint(10,100)

def countdown():
  for i in range(num):
    print(i+1)

print("Countdown")
tt.add_entry()