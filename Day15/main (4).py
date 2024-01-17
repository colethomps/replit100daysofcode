exit =""
animal =""
while exit!="yes" and exit!="Yes":
    animal = input("What animal do you want? :")
    if animal == "dog" or animal == "Dog":
      print("Woof")
    elif animal == "cat" or animal == "Cat":
      print("Meow")
    elif animal == "bird" or animal == "Bird":
      print("Tweet, Kaka, Chirp")
    else:
      print("I don't know that animal")
    exit = input("Do you want to exit? :")