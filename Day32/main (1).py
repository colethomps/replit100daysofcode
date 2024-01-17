import random
greeting = ["Hello","Hola","Bonjour","Salut","Hallo","Ciao","Ni Hao","Ola","Konni"]
randint = random.randint(0,(len(greeting)-1))

print(f"{greeting[randint]}!")