import requests, json
import os

jokes = []
while True:
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) # get a random dad joke from the site endpoint and assign to a variable. The second argument (the header request) tells the script to return the json data as a string.
  joke = result.json()
  print(joke["joke"])
  inputer = ""
  inputer = input("Save, load, new?")
  os.system("clear")
  if inputer.lower() == "save":
    print("Saved.")
    jokes.append(joke)
  elif inputer.lower() == "load":
    print(jokes)
  elif inputer.lower() == "new":
    continue
  else:
    break