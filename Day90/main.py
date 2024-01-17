import requests, json
# print(json.dumps(user, indent=2)) 
for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  user = result.json()
  for person in user['results']: #loops through each person in the results dictionary
    name = f"""{person["name"]["first"]} {person["name"]["last"]}""" #creates a string with the name of the person
    image = f"""{person["picture"]["medium"]}""" #creates a string with the image of the person
    print(name)#prints the name of the person