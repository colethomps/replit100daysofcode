import random
import time
import os

def hp():
    return (((random.randint(1, 6)) * (random.randint(1, 12))) / 2) + 10

def strength():
    return (((random.randint(1, 6)) * (random.randint(1, 12))) / 2) + 12

def character():
    time.sleep(0.5)
    name = input("Name Your Legend: ")
    time.sleep(0.5)
    os.system("clear")
    char_type = input("Character Type: ")
    time.sleep(0.5)
    os.system("clear")
    print(name, "the", char_type)
    character_hp = hp()
    character_strength = strength()
    print("Health:", character_hp)
    print("Strength:", character_strength)
    return name, char_type, character_hp, character_strength

def character2():
    time.sleep(0.5)
    name = input("Name Your Legend: ")
    time.sleep(0.5)
    os.system("clear")
    char_type = input("Character Type: ")
    time.sleep(0.5)
    os.system("clear")
    print(name, "the", char_type)
    character_hp = hp()
    character_strength = strength()
    print("Health:", character_hp)
    print("Strength:", character_strength)
    return name, char_type, character_hp, character_strength

print("Character Builder")
time.sleep(0.5)
os.system("clear")
character1_data = character()
time.sleep(5)
print()
print("Who are the Battling?")
print()
character2_data = character2()
time.sleep(5)
os.system("clear")

char1_name, char1_type, char1_hp, char1_strength = character1_data
char2_name, char2_type, char2_hp, char2_strength = character2_data

round = 0
if char1_strength>char2_strength:
  strengthDiff = char1_strength-char2_strength
elif char1_strength<char2_strength:
  strengthDiff = char2_strength-char1_strength
else:
  strengthDiff = 0

while True:
    os.system("clear")
    print("⚔️ Battle Time ⚔️")
    char1_die = random.randint(1, 6)
    char2_die = random.randint(1, 6)
    round += 1

    print("The Battle Begins")

    if char1_die > char2_die:
        char2_hp -= (strengthDiff) + 1
        print(char1_name, "wins the", round, "round, with", strengthDiff+1, "strength damage")
    elif char1_die < char2_die:
        char1_hp -= (strengthDiff) + 1
        print(char2_name, "wins the", round, "round, with", strengthDiff+1, "strength damage")
    else:
        print("No damage done")

    print(char1_name, "has", char1_hp, "health")
    print(char2_name, "has", char2_hp, "health")
    time.sleep(2)
    if char1_hp <= 0:
        print(char1_name, "has lost the battle in",round,"rounds!")
        break
    elif char2_hp <= 0:
        print(char2_name, "has lost the battle in",round,"rounds!")
        break
    else:
        continue
    
