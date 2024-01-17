import random

class character:
  name = None
  health = None
  magicPoints = None

  def __init__(self, name, health, magicPoints):
    self.name = name
    self.health = health
    self.magicPoints = magicPoints

class player(character):
  def __init__(self):
    self.name = "David"
    self.health = random.randint(0,100)
    self.magicPoints = random.randint(0,100)
    self.lives = 3

class enemy(character):
  def __init__(self):
    self.name = "Enemy"
    self.health = random.randint(0,100)
    self.magicPoints = random.randint(0,100)
    self.type = random.choice(["orc", "vampire"])
    self.strength = random.randint(0,100)

  def orc(self):
      self.type = "Orc"
      self.strength = random.randint(0,100)
      self.speed = random.randint(0,100)

  def vampire(self):
      self.type = "Vampire"
      self.strength = random.randint(0,100)
      self.dayNight = random.choice(["day", "night"])

player_instance = player()
print("Player")
print("Name: ", player_instance.name)
print("Health: ", player_instance.health)
print("Magic Points: ", player_instance.magicPoints)
print("Lives: ", player_instance.lives)
print("")

for i in range(2):
  enemy_instance = enemy()
  enemy_instance.orc()
  print("Enemy")
  print("Name: ", enemy_instance.name)
  print("Health: ", enemy_instance.health)
  print("Magic Points: ", enemy_instance.magicPoints)
  print("Type: ", enemy_instance.type)
  print("Strength: ", enemy_instance.strength)
  print("")
for i in range(2):
  enemy_instance = enemy()
  enemy_instance.vampire()
  print("Enemy")
  print("Name: ", enemy_instance.name)
  print("Health: ", enemy_instance.health)
  print("Magic Points: ", enemy_instance.magicPoints)
  print("Type: ", enemy_instance.type)
  print("Strength: ", enemy_instance.strength)
  print("Day/Night: ", enemy_instance.dayNight)
  print("")