import random
import time
import os

class Player:
# To create a player instance, give the input for name.
  def __init__(self, name, ring=False, sword=False, boots=False, flee_chance=False, health=80, potions=0):
    self.name = name
    self.health = health
    self.is_dead = False
    self.flee_chance = flee_chance
    self.ring = ring
    self.sword = sword
    self.boots = boots
    self.potions = potions

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
    if foyer_case_knife == False:
      print("\nWhat a cheap way to go. These game developers are some punks.")

    quit()

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
                 
                    """)
      time.sleep(2) 

    else:
      print("""You tripped on a rock!""")

  def make_friends(self):
    #Easter egg, secret option to end the game with some dialogue.
    os.system('clear||cls')  
    print("""You ask the Jelly how it is doing today. 
            \nThe Jelly has a lot on it's mind, such as what is the purpose of life
            and the existential crises the Jelly faces. 
            The Jelly tells you about it's family and how it never 
            has time to do the things it wants to get done.
            You can relate to the Jelly.  
            It turns out you and the Jelly have a lot of interests in common,
            such as art, music, sports, and academic pursuits. 
            You and the Jelly exchange numbers and friend each other 
            on the various social media platforms.  
            As you realize we all have our struggles, you bid farewell to the Jelly 
            and wish it the best in it's Jelly life.
            YOU MAKE FRIENDS WITH THE JELLY. 
            
            Thank you for playing!.....:)""")
    quit() 

    
  def lose_health(self, amount):
  # Deducts health from a character and prints the health remaining. If player is wearing ring, damage is reduced by 1/3.
    self.health -= amount
    if self.health <= 0:
      self.death()
    else:
      print("{name} has {health} HP remaining.".format(name = self.name, health = self.health))
  
  def attack(self, enemy):
  # Selects a random number from range 1-6 and if 1, attack will miss the jelly. Otherwise, selects a random number from range 5-15 and uses the value in the lose_health function. If player has sword then damage increases by 1.5.
    miss = 1
    if random.randint(1,6) == miss:                                      
      damage = 0
      print("{} misses the {} Jelly!".format(self.name, enemy.element))
    else:
      if self.sword == True:
        damage = round(random.randint(5,15) * 1.5)
        print("{name} uses the Butterknife of Truth! The {element} Jelly suffers {damage} HP damage.".format(name=self.name, element=enemy.element, damage=damage))
        enemy.lose_health(damage)
      else:
        damage = random.randint(5,15)
        print("{name} attacks the {element} Jelly! The {element} Jelly suffers {damage} HP damage.".format(name=self.name, element=enemy.element, damage=damage))
        enemy.lose_health(damage)

  def use_potion(self):
    if self.potions > 0:
      self.health += 30
      self.potions -= 1
      print(f"{self.name} uses a potion! {self.name}'s HP increases by 30.\n{self.name} has {self.health} HP remaining.")
      time.sleep(0.5)
      print(f"{self.name} has {self.potions} potions remaining.")
    elif self.potions == 0:
      print("You reach for a potion, but your bag is empty!")
   

      
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
    if random.randint(1,6) == 1:
      damage = 0
      print("The {} Jelly misses {}!".format(self.element, player.name))
    else:
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
    time.sleep(1)
    print(f"\nThe {jelly_1.element} Jelly has been defeated.")
    
    print("""
             Y   Y  OOO  U   U    W   W IIIII N   N
              Y Y  O   O U   U    W   W   I   NN  N
               Y   O   O U   U    W W W   I   N N N
               Y   O   O U   U    WW WW   I   N  NN
               Y    OOO   UUU     W   W IIIII N   N  
               """)

    time.sleep(1)
    print(f"{player_1.name} has {player_1.health} HP remaining.")
    input("Press 'Enter' to continue...")
    os.system('clear||cls')

# Setting up room functions for movement and game progression
def dungeon_cave_potion_in_room():
    global dungeon_cave_potion
    potion_list = ['yes', 'no']
    potion_choice = input("Will you pick up the flask? Please type 'yes' or 'no'.").lower()
    while potion_choice not in potion_list:
        potion_choice = input("Sorry, that is not a valid option.\nWill you pick up the flask? Please type 'yes' or 'no'.").lower()
    if potion_choice == 'yes':
        player_1.potions += 1 
        print(f"{player_1.name} now has {player_1.potions} potions.")
        time.sleep(2)
        dungeon_cave_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{player_1.name} now has {player_1.potions} potions.")
        time.sleep(2)

def dungeon_cave():
  global jelly_1
  global dungeon_cave_counter
  global dungeon_cave_potion
  if dungeon_cave_counter > 0:
    os.system('clear||cls')
    print("You are back in what you assume to be the castle dungeon cave.\nBest not to dilly dally about.")
    if dungeon_cave_potion == True:
        print("You see the flask on the ground from earlier.")
        dungeon_cave_potion_in_room()
        os.system('clear||cls')
        print("You decide it's time to leave. You climb the ladder and return to the armory.")
        input("Press 'Enter' to continue...")
        armory()
    elif dungeon_cave_potion == False:
        print("You decide it's time to leave. You climb the ladder and return to the armory.")
        input("Press 'Enter' to continue...") 
        armory()
  elif dungeon_cave_counter == 0:
    os.system('clear||cls')
    print("You are surrounded in total darkness. You look at your arms, in shackles,\nwondering if you'll ever escape. Luckily, the wrist compass your father got you for your birthday is still intact.\nYou hear something fall on the ground next to you.\nSomeone dropped a key from a small hole in the rock above!\nYou unlock your shackles and look around the dark damp cave. You see a flask on the ground.")
    dungeon_cave_potion_in_room()
    print("A Jelly approaches!".upper()) 
    print("It appears to be a {element} Jelly.".format(element=jelly_1.element))
    time.sleep(1)
    battle_loop()
    os.system('clear||cls')
    print("You decide it's time to get moving, you see a ladder with a small hatch at the top.")
    print("You open the hatch and enter the next room.")
    input("Press 'Enter' to continue...")
    dungeon_cave_counter += 1 
    jelly_2 = Jelly()
    jelly_2.select_element()
    jelly_1 = jelly_2  
    time.sleep(2)
    armory()

def armory_sword_in_room():
    global armory_sword
    sword_list = ['yes', 'no']
    sword_choice = input("Will you pick up the sword? Please type 'yes' or 'no'.").lower()
    while sword_choice not in sword_list:
        sword_choice = input("Sorry, that is not a valid option.\nWill you pick up the sword? Please type 'yes' or 'no'.").lower()
    if sword_choice == 'yes':
        player_1.sword = True  
        print(f"{player_1.name} now has the Butterknife of Truth! Time to spread some Jelly.")
        time.sleep(2)
        armory_sword = False  
    elif sword_choice == 'no':
        player_1.sword = False
        print(f"{player_1.name} has left the sword for now.")
        time.sleep(2)

def armory():
    global jelly_1
    global armory_counter
    global armory_sword 
    if armory_counter > 0:
        os.system('clear||cls')
        print("You are back in the Jelly castle armory.\nThings are quiet, for now...")
        if armory_sword == True:
            print("You see the sword on the rack from earlier.")
            armory_sword_in_room()
            os.system('clear||cls')
            print("You decide it's time to leave. Which way will you go?")
            choice = input("Type 'dungeon' to return to the Dungeon or type 'door' to head through the ornate door.").lower()
            while choice != 'dungeon' and choice != 'door':
              choice = input("Sorry, that is not a valid option. Please type 'dungeon' or 'door'.").lower()
            if choice == 'dungeon':
                dungeon_cave()
            elif choice == 'door':
                dining_hall()
        elif armory_sword == False:
            print("You decide it's time to leave. Which way will you go?")
            choice = input("Type 'dungeon' to return to the Dungeon or type 'door' to head through the ornate door.").lower()
            while choice != 'dungeon' and choice != 'door':
              choice = input("Sorry, that is not a valid option. Please type 'dungeon' or 'door'.").lower()
            if choice == 'dungeon':
                dungeon_cave()
            elif choice == 'door':
                dining_hall()
    elif armory_counter == 0:
        os.system('clear||cls')
        print("You take a look around a dimly lit room. You see various armaments such as\nswords and bows, and armor that looks too small for you to wear, probably designed with a Jelly in mind.\nOne sword in particular piques your interest.  As you approach the sword, you see the fine\ncraftsmanship and the ornate jewel encrusted hilt.  What a fine sword.")
        armory_sword_in_room()
        print("A Jelly approaches!".upper())
        print("It appears to be a {element} Jelly.".format(element=jelly_1.element))
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Well, no time to waste. You see an ornate door leading from the armory.\nAlso behind you is the ladder leading back to the dungeon below.\nWhich way will you go?")
        armory_counter += 1 
        jelly_3 = Jelly()
        jelly_3.select_element()
        jelly_1 = jelly_3
        choice = input("Type 'dungeon' to return to the Dungeon or type 'door' to head through the ornate door.").lower()
        while choice != 'dungeon' and choice != 'door':
              choice = input("Sorry, that is not a valid option. Please type 'dungeon' or 'door'.").lower()
        if choice == 'dungeon':
            dungeon_cave()
        elif choice == 'door':
            dining_hall()
        time.sleep(2)

def dining_hall_potions_in_room():
    global dining_hall_potions
    potion_list = ['yes', 'no']
    potion_choice = input("Will you pick up the potions? Please type 'yes' or 'no'.").lower()
    while potion_choice not in potion_list:
        potion_choice = input("Sorry, that is not a valid option.\nWill you pick up the potions? Please type 'yes' or 'no'.").lower()
    if potion_choice == 'yes':
        player_1.potions += 2  
        print(f"{player_1.name} now has {player_1.potions} potions.")
        time.sleep(2)
        dining_hall_potions = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{player_1.name} now has {player_1.potions} potions.")
        time.sleep(2)

def dining_hall():
    global jelly_1
    global dining_hall_counter
    global dining_hall_potions
    list_of_choices = ['armory', 'n', 's', 'g']
    if dining_hall_counter > 0:
        os.system('clear||cls')
        print("You are back in the spacious dining hall.\nIt seems no one has noticed the commotion going on.\nThe smell of fresh rolls makes your belly rumble.")
        if dining_hall_potions == True:
            print("You see the two potions on the table from earlier.")
            dining_hall_potions_in_room()
            os.system('clear||cls')
            print("You decide it's time to leave. You see the armory door, to the north is a set of double doors,\nto the south is a set of double doors with fresh roll smell coming from them,\nand to the west is a set of gold doors.\nWhich way will you go?")
            choice = input("Type 'armory' to return to the armory, 'n' for north doors,\n's' for south doors or\n'g' for gold doors.").lower()
            while choice not in list_of_choices:
              choice = input("Sorry, that is not a valid option. Please type 'armory', 'n', 's', or 'g'.").lower()
            if choice == 'armory':
                armory()
            elif choice == 'n':
                foyer()
            elif choice == 's':
              kitchen()
            elif choice == 'g':
              throne_room()
        elif dining_hall_potions == False:
            print("You decide it's time to leave. You see the armory door, to the north is a set of double doors,\nto the south is a set of double doors with fresh roll smell coming from them,\nand to the west is a set of gold doors.\nWhich way will you go?")
            choice = input("Type 'armory' to return to the armory, 'n' for north doors,\n's' for south doors or\n'g' for gold doors.").lower()
            while choice not in list_of_choices:
              choice = input("Sorry, that is not a valid option. Please type 'armory', 'n', 's', or 'g'.").lower()
            if choice == 'armory':
                armory()
            elif choice == 'n':
                foyer()
            elif choice == 's':
              kitchen()
            elif choice == 'g':
              throne_room()
    elif dining_hall_counter == 0:
        os.system('clear||cls')
        print("As you enter, you see a grand hall with a giant table in the center.\nGiant chandeliers hang from the thirty-foot celing, and paintings of Jellies adorn the room.\nThere appears to be about fifty chairs at the table, with a large decorative chair at the head of the table.\nThe table has been set for a grand meal, as you see plates and silverware on the table.\nYou notice the faint smell of fresh rolls. You see there are a couple of potions on the table.")
        dining_hall_potions_in_room()
        print("A Jelly approaches!".upper())
        print("It appears to be a {element} Jelly.".format(element=jelly_1.element))
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Well, that was intense! Time to bounce. You see the armory door to the east.\nTo the north is a set of double doors, and to the south is a set of doors with faint fresh roll smell coming from them.\nTo the west is a large set of golden double doors. Which way will you go?")
        dining_hall_counter += 1 
        jelly_4 = Jelly()
        jelly_4.select_element()
        jelly_1 = jelly_4
        choice = input("Type 'armory' to return to the armory, 'n' for north doors,\n's' for south doors or\n'g' for gold doors.").lower()
        while choice not in list_of_choices:
            choice = input("Sorry, that's not a valid option. Type 'armory' to return to the armory, 'n' for north doors,\n's' for south doors or\n'g' for gold doors.").lower()
        if choice == 'armory':
          armory()
        elif choice == 'n':
          foyer()
        elif choice == 's':
          kitchen()
        elif choice == 'g':
          throne_room()
        time.sleep(2)

def foyer_case_knife_in_room():
    global foyer_case_knife
    sword_list = ['yes', 'no']
    sword_choice = input("Will you pick up the case knife? Please type 'yes' or 'no'.").lower()
    while sword_choice not in sword_list:
        sword_choice = input("Sorry, that is not a valid option.\nWill you pick up the case knife? Please type 'yes' or 'no'.").lower()
    if sword_choice == 'yes':
        print(f"{player_1.name} now has the Case Knife of Deception!")
        time.sleep(2)
        print("\nTHE KNIFE IS POISONED.")
        time.sleep(2)
        foyer_case_knife = False 
        player_1.death()
    elif sword_choice == 'no':
        foyer_case_knife = True
        print(f"{player_1.name} has left the case knife for now.")
        time.sleep(2)

def foyer():
    global jelly_1
    global foyer_counter
    global foyer_case_knife
    list_of_choices = ['d', 'e', 'exit']
    if foyer_counter > 0:
        os.system('clear||cls')
        print("You are back in the castle foyer.\nFreedom is within your reach!\nYou don't see anything that could impede your escape.")
        if foyer_case_knife == True:
            print("You see the case knife on the entryway table from earlier.")
            foyer_case_knife_in_room()
            os.system('clear||cls')
            print("You figure you better hurry, freedom is within your grasp. You see the dining hall doors, \nto the east is a set of open double doors with what looks to be a stage with curtains in a large hall,\nto the north is a set of giant doors exiting the castle, leading to a drawbridge.\nWhich way will you go?")
            choice = input("Type 'd' to return to the dining hall, 'e' for the doors with a visible stage through them to the east,\nor 'exit' for the doors leading to the drawbridge.").lower()
            while choice not in list_of_choices:
              choice = input("Sorry, that is not a valid option. Please type 'd', 'e', or 'exit'.").lower()
            if choice == 'd':
                dining_hall()
            elif choice == 'e':
                theater()
            elif choice == 'exit':
              drawbridge()
        elif foyer_case_knife == False:
            player_1.death()
    elif foyer_counter == 0:
        os.system('clear||cls')
        print("You walk into the castle foyer. The beautiful marble floor reflects the sunlight shining in from the balcony.\nYou see a grand staircase leading up to the balcony. There is a table in the center\nof the room with a fantastic floral arrangement. Small comfy looking benches line the edges of the circular room.\nThe exit of the castle is in front of you, leading to a drawbridge.\nTo the east is a set of open doors. You can see a large hall and a stage with red curtains in the hall.\nOn the table with the floral arrangement, something shiny catches your eye.\nA small case knife sits on the table.")
        foyer_case_knife_in_room()
        print("A Jelly approaches!".upper())
        print("It appears to be a {element} Jelly. It's the last thing standing between you and freedom.".format(element=jelly_1.element))
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("A sense of relief falls over you. Freedom is just a few yards away. The castle exit is before you.\nTo the east is a set of open double doors, with what appears to be a theater inside.\nBehind you is the dining hall. Where will you go?")
        foyer_counter += 1 
        jelly_5 = Jelly()
        jelly_5.select_element()
        jelly_1 = jelly_5
        choice = input("Type 'd' to return to the dining hall, 'e' for the doors with a visible stage through them to the east,\nor 'exit' for the doors leading to the drawbridge.").lower()
        while choice not in list_of_choices:
            choice = input("Sorry, that is not a valid option.\nType 'd' to return to the dining hall, 'e' for the doors with a visible stage through them to the east,\nor 'exit' for the doors leading to the drawbridge.").lower()
        if choice == 'd':
          dining_hall()
        elif choice == 'e':
          theater()
        elif choice == 'exit':
          drawbridge()
        time.sleep(2)        

def kitchen_potion_in_room():
    global kitchen_potion 
    potion_list = ['yes', 'no']
    potion_choice = input("Will you pick up the potion? Please type 'yes' or 'no'.").lower()
    while potion_choice not in potion_list:
        potion_choice = input("Sorry, that is not a valid option.\nWill you pick up the potion? Please type 'yes' or 'no'.").lower()
    if potion_choice == 'yes':
        player_1.potions += 1  
        print(f"{player_1.name} now has {player_1.potions} potions.")
        time.sleep(2)
        kitchen_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{player_1.name} now has {player_1.potions} potions.")
        time.sleep(2)


def kitchen():
    global jelly_1
    global kitchen_counter
    global kitchen_potion 
    if kitchen_counter > 0:
        os.system('clear||cls')
        print("You are back in the castle kitchen.\nThings are calm, except for the rumbling of your belly. Those rolls smell so good.")
        if kitchen_potion == True:
            print("You see the potion on the counter from earlier.")
            kitchen_potion_in_room()
            os.system('clear||cls')
            print("It smells so good in here. You're starving, but no time to waste. Which way will you go?")
            choice = input("Type 'n' to return north to the dining hall or type 'w' to head west\nthrough the small door where you see many small beds, presumably the staff quarters.").lower()
            while choice != 'n' and choice != 'w':
              choice = input("Sorry, that is not a valid option. Please type 'n' or 'w'.").lower()
            if choice == 'n':
                dining_hall()
            elif choice == 'w':
                staff_quarters()
        elif kitchen_potion == False:
            print("It smells so good in here. You're starving, but no time to waste. Which way will you go?")
            choice = input("Type 'n' to return north to the dining hall or type 'w' to head west\nthrough the small door where you see many small beds, presumably the staff quarters.").lower()
            while choice != 'n' and choice != 'w':
              choice = input("Sorry, that is not a valid option. Please type 'n' or 'w'.").lower()
            if choice == 'n':
                dining_hall()
            elif choice == 'w':
                staff_quarters()
    elif kitchen_counter == 0:
        os.system('clear||cls')
        print("As you enter the room, you smell fresh rolls, just like your mom used to bake.\nThere is a huge ice box full of various meats and milk.\nYou see a wine rack with too many different wines to count.\nIt looks like a giant pot pie is cooking on the stove.\nIt smells delicious. You notice a potion sitting on the kitchen counter.")
        kitchen_potion_in_room()
        print("The smell is too good. You can't help yourself any longer.\nYou reach for the pot pie, but before you can take a bite,")
        time.sleep(1)
        print("A Jelly approaches!".upper())
        time.sleep(1)
        print("It has a chef's apron and hat.")
        print("It appears to be a {element} Jelly.".format(element=jelly_1.element))
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Well, no time to eat after all. You see a small door to the west\nwhere you can see many small beds inside. Probably the staff quarters.\nTo the north are the doors leading back to the dining hall.\nWhich way will you go?")
        kitchen_counter += 1 
        jelly_6 = Jelly()
        jelly_6.select_element()
        jelly_1 = jelly_6
        choice = input("Type 'n' to return north to the dining hall or type 'w' to head west\nthrough the small door where you see many small beds, presumably the staff quarters.").lower()
        while choice != 'n' and choice != 'w':
              choice = input("Sorry, that is not a valid option. Please type 'n' or 'w'.").lower()
        if choice == 'n':
            dining_hall()
        elif choice == 'w':
            staff_quarters()
        time.sleep(2)


  

def throne_room():
  pass

def staff_quarters():
  pass

def royal_quarters():
  pass

def theater():
  pass

def drawbridge():
  pass

def forest():
  pass





  

def battle_loop():
    while player_1.health > 0 and jelly_1.health > 0:
        choice_list = ['attack', 'run', 'potion', 'make friends']
        choice = input("Please type 'attack', 'run', or 'potion'.  ")
        if choice not in choice_list:
            time.sleep(0.5)
            print("Ha Ha, you're funny. Sorry, that's not an available option."  )
        elif choice == "make friends":
            time.sleep(1)
            player_1.make_friends()
            
        elif choice == "attack":
            time.sleep(0.5)
            player_1.attack(jelly_1)
            time.sleep(1)
            if jelly_1.health > 0:
                time.sleep(0.5)
                jelly_1.attack(player_1)
                time.sleep(0.5)
        elif choice == "potion":
            time.sleep(0.5)
            player_1.use_potion()
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
 
# Naming the player and initiating JellyBattle
player_one_name = input("Welcome to the world of JellyBattle! Please type your character name then press enter.  ")
time.sleep(0.5)
print("Hello " + str(player_one_name) + "! It is time to begin your adventure.")
time.sleep(2)
# Creating instances
player_1 = Player(player_one_name)
jelly_1 = Jelly()
jelly_1.select_element()
# Room and item counters for backtracking rooms
dungeon_cave_counter = 0
dungeon_cave_potion = True
armory_counter = 0
armory_sword = True 
dining_hall_counter = 0
dining_hall_potions = True
foyer_counter = 0
foyer_case_knife = True 
kitchen_counter = 0
kitchen_potion = True 
dungeon_cave()








item_list = ['sword', 'ring', 'none']
item_choice = input("\nYou look at the nearby table and see a sword and a ring on the table. \nYou decide to pick one of the items up.\nWhich one do you grab?\nPlease type 'sword', 'ring', or 'I don't need a crutch. I'm taking this jelly on barehanded!'(just type 'none' in that case).")
while item_choice not in item_list:
  item_choice = input("Ha Ha, you're funny. Sorry, that's not an available option. Please type 'sword', 'ring', or 'none'."  )
if item_choice == 'sword':
  player_1.sword = True
  print("You picked up the Butterknife of Truth! Time to spread some jelly!")
if item_choice == 'ring':
  player_1.ring = True
  print("You picked up the Ring of Defense!")
if item_choice == 'none':
  player_1.ring == False

# Main game loop

        
    
        
 