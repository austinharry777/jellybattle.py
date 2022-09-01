import random
import time
import os

class Player:
# To create a player instance, give the input for name.
  def __init__(self, name, ring=False, sword=False, flee_chance=False, health=50):
    self.name = name
    self.health = health
    self.is_dead = False
    self.flee_chance = flee_chance
    self.ring = ring
    self.sword = sword

  def __repr__(self):
    # Printing a character will tell you the character's name and how much health they have left.
    return "{name} has {health} HP remaining.".format(name = self.name, health = self.health)

  def death(self):
    # When a character's health is reduced to 0, the is_dead status will flip to True, the character will die and the game ends.
    self.is_dead = True
    print("""  
               Y   Y  OOO  U   U    DDDD  IIIII EEEEE DDDD 
                Y Y  O   O U   U    D   D   I   E     D   D
                 Y   O   O U   U    D   D   I   EEE   D   D
                 Y   O   O U   U    D   D   I   E     D   D
                 Y    OOO   UUU     DDDD  IIIII EEEEE DDDD  """)

  def flee(self):
  # Generates a random number and gives the player a 25% chance of escaping the battle
    if random.randint(1,4) == 1:
      self.flee_chance = True
      print("""
      
               Y   Y  OOO  U   U    RRRR    A   N   N
                Y Y  O   O U   U    R   R  A A  NN  N
                 Y   O   O U   U    RRRR  AAAAA N N N   
                 Y   O   O U   U    R  R  A   A N  NN
                 Y    OOO   UUU     R   R A   A N   N   
                 
                 (And they laughed at you...:)   """)
    else:
      print("""You tripped on a rock!""")

  def make_friends(self):
    #Easter egg, secret option to end the game with some dialogue.
    os.system('clear||cls')
    print("""You ask the Jelly how it is doing today. 
            The Jelly has a lot on it's mind, such as what is the purpose of life
            and the existential crises the Jelly faces. 
            The Jelly tells you about it's family and how it never 
            has time to do the things it wants to get done.
            You can relate to the Jelly.  It turns out you and the Jelly have a lot of interests in common,
            such as art, music, sports, and academic pursuits. 
            You and the Jelly exchange numbers and friend each other on the various social media platforms.  
            As you realize we all have our struggles, you bid farewell to the Jelly 
            and wish it the best in it's Jelly life.
            YOU MAKE FRIENDS WITH THE JELLY. 
            
            Thank you for playing!.....:)""")
    
  def lose_health(self, amount):
  # Deducts health from a character and prints the health remaining. If player is wearing ring, damage is reduced by 1/3.
    self.health -= amount
    if self.health <= 0:
      self.death()
    else:
      print("{name} has {health} HP remaining.".format(name = self.name, health = self.health))
  
  def attack(self, enemy):
  # Selects a random number from range 5-15 and uses the value in the lose_health function. If player has sword then damage increases by 1.5.
    if self.sword == True:
      damage = round(random.randint(5,15) * 1.5)
      print("{name} uses the Butterknife of Truth! The {element} Jelly suffers {damage} HP damage.".format(name=self.name, element=enemy.element, damage=damage))
      enemy.lose_health(damage)
    else:
      damage = random.randint(5,15)
      print("{name} attacks the {element} Jelly! The {element} Jelly suffers {damage} HP damage.".format(name=self.name, element=enemy.element, damage=damage))
      enemy.lose_health(damage)

class Jelly:
# The Jelly instance is automatically created upon program initiation.
  def __init__(self, element=None, health = 40):
    self.health = health
    self.element = element
    self.is_dead = False
  
  def __repr__(self):
    # Printing a jelly will tell you how much health the jelly has left.
    return "The Jelly has {health} HP remaining.".format(health = self.health)

  def select_element(self):
    list_of_elements = ["Fire", "Water", "Wind", "Earth", "Strawberry", "Grape", "Ubiquitous", "Peanut Butter"]
    self.element = random.choice(list_of_elements)

  
  def lose_health(self, amount):
  # Deducts health from a jelly and prints the health remaining
    self.health -= amount
    if self.health <= 0:
      self.victory()
    else:
      print("The {element} Jelly has {health} HP remaining.".format(element=self.element, health = self.health))
  
  def attack(self, player):
  # Selects a random number from range 5-15 and uses the value in the lose_health function. Adds an additional amount of damage if jelly element is Earth, Wind, Fire, or Water.
    if player.ring == True:
        print("The Ring of Defense has Activated!")  
        damage = round(random.randint(5,15) / 1.5)
        damage_elements = ["Fire", "Water", "Wind", "Earth"] 
        print("The {element} Jelly attacks! {name} suffers {damage} HP damage.".format(element=self.element, name=player.name, damage=damage))
        if self.element in damage_elements:
            elemental_damage = round(random.randint(1, 5) / 1.5) 
            damage += elemental_damage
            print("{name} suffers an additional {damage} HP of {element} damage.".format(name=player_1.name, damage=elemental_damage, element=self.element))
            player.lose_health(damage)
        else:
            player.lose_health(damage)
    elif player.ring == False:
        damage = random.randint(5,15)
        damage_elements = ["Fire", "Water", "Wind", "Earth"] 
        print("The {element} Jelly attacks! {name} suffers {damage} HP damage.".format(element=self.element, name=player.name, damage=damage))
        if self.element in damage_elements:
            elemental_damage = random.randint(1, 5) 
            damage += elemental_damage
            print("{name} suffers an additional {damage} HP of {element} damage.".format(name=player_1.name, damage=elemental_damage, element=self.element))
            player.lose_health(damage)
        else:
            player.lose_health(damage)
      
    
  
  def victory(self):
  # If player defeats the Jelly, they get a victory message.  
    print("""
             Y   Y  OOO  U   U    W   W IIIII N   N
              Y Y  O   O U   U    W   W   I   NN  N
               Y   O   O U   U    W W W   I   N N N
               Y   O   O U   U    WW WW   I   N  NN
               Y    OOO   UUU     W   W IIIII N   N  """)
  
# Naming the player and initiating JellyBattle
player_one_name = input("Welcome to the world of JellyBattle! Please type your character name then press enter.  ")
time.sleep(0.5)
print("Hello " + str(player_one_name) + "! It is time to begin. You are wandering outside town when.... \na JELLY APPEARS!")

# Creating instances
player_1 = Player(player_one_name)
jelly_1 = Jelly()
jelly_1.select_element()
print("It appears to be a {element} Jelly.".format(element=jelly_1.element))
item_choice = input("\nYou look at the nearby table and see a sword and a ring on the table. \nYou decide to pick one of the items up.\nWhich one do you grab?\nPlease type 'sword' or 'ring'.")
if item_choice != 'sword' and item_choice != 'ring':
  print("Ha Ha, you're funny. Sorry, that's not an available option."  )
elif item_choice == 'sword':
  player_1.sword = True
  print("You picked up the Butterknife of Truth! Time to spread some jelly!")
elif item_choice == 'ring':
  player_1.ring = True
  print("You picked up the Ring of Defense!")


# Main game loop
while player_1.health > 0 and jelly_1.health > 0:
  choice = input("Please type 'attack' or 'run'.  ")
  if choice != "attack" and choice != "run" and choice != "make friends":
    time.sleep(0.5)
    print("Ha Ha, you're funny. Sorry, that's not an available option."  )
  elif choice == "make friends":
    time.sleep(1)
    player_1.make_friends()
    break
  elif choice == "attack":
    time.sleep(0.5)
    player_1.attack(jelly_1)
    time.sleep(1)
    if jelly_1.health > 0:
      time.sleep(0.5)
      jelly_1.attack(player_1)
      time.sleep(0.5)
  elif choice == "run":
    time.sleep(0.5)
    player_1.flee()
    if player_1.flee_chance == True:
      break
    if jelly_1.health > 0:
      time.sleep(0.5)
      jelly_1.attack(player_1)
      time.sleep(0.5)

  else: 
    player_1.death() or jelly_1.victory()
    break
 