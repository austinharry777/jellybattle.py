import random
import time
import os
from colorama import Fore, Back, Style

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

class Player:
# To create a player instance, give the input for name.
  def __init__(self, name, monocle=False, note=False, ring=False, sword=False, axe=False, boots=False, flee_chance=False, ally=False, health=200, potions=0, attack_lvl=1, defense_lvl=1, level=1, xp=0, booty_bomb = False, is_poisoned = False):
    self.name = name
    self.health = health
    self.is_dead = False
    self.flee_chance = flee_chance
    self.ring = ring
    self.sword = sword
    self.axe = axe 
    self.boots = boots
    self.potions = potions
    self.note = note 
    self.monocle = monocle 
    self.ally = ally
    self.attack_lvl = attack_lvl
    self.defense_lvl = defense_lvl
    self.level = level
    self.xp = xp 
    self.booty_bomb = booty_bomb 
    self.is_poisoned = is_poisoned
  def __repr__(self):
    # Printing a character will tell you the character's name and how much health they have left.
    return "{name} has {health} HP remaining.".format(name = self.name, health = self.health)

  def gain_xp(self, amount):
    self.xp += amount
    print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has gained {Fore.CYAN}{amount} experience points.{Style.RESET_ALL}")
    if self.xp >= 30:
      self.level_up()
      self.xp = 0

  #Function to allow player to increase attack, defense, or add an element to the Axe of Preserves.
  def level_up(self):
    global player_axe_elements
    self.level += 1
    level_choice = ['a', 'f', 'i', 'wa', 't', 'e', 'wi', 'd']
    if self.axe == True:
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has leveled up! {Fore.CYAN}{self.name}{Style.RESET_ALL} is now {Fore.CYAN}level {self.level}{Style.RESET_ALL}.")
      choice = input(f"You may level up an attribute. Press {Fore.MAGENTA}'a'{Style.RESET_ALL} to boost attack,{Fore.MAGENTA}'d'{Style.RESET_ALL} to boost defense, or you can add an element to your {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}\nPress {Fore.MAGENTA}'f'{Style.RESET_ALL} for {Fore.LIGHTRED_EX}Fire,{Style.RESET_ALL} {Fore.MAGENTA}'i'{Style.RESET_ALL} for {Fore.CYAN}Ice,{Style.RESET_ALL} {Fore.MAGENTA}'wa'{Style.RESET_ALL} for {Fore.CYAN}Water,{Style.RESET_ALL} {Fore.MAGENTA}'t'{Style.RESET_ALL} for {Fore.LIGHTYELLOW_EX}Thunder,{Style.RESET_ALL} {Fore.MAGENTA}'e'{Style.RESET_ALL} for {Fore.MAGENTA}Earth,{Style.RESET_ALL} or {Fore.MAGENTA}'wi'{Style.RESET_ALL} for {Fore.LIGHTGREEN_EX}Wind.{Style.RESET_ALL}").lower()
      while choice not in level_choice:
        choice = input(f"Sorry, that is not an option. Press {Fore.MAGENTA}'a'{Style.RESET_ALL} to boost attack,{Fore.MAGENTA}'d'{Style.RESET_ALL} to boost defense, or you can add an element to your {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}\nPress {Fore.MAGENTA}'f'{Style.RESET_ALL} for {Fore.LIGHTRED_EX}Fire,{Style.RESET_ALL} {Fore.MAGENTA}'i'{Style.RESET_ALL} for {Fore.CYAN}Ice,{Style.RESET_ALL} {Fore.MAGENTA}'wa'{Style.RESET_ALL} for {Fore.CYAN}Water,{Style.RESET_ALL} {Fore.MAGENTA}'t'{Style.RESET_ALL} for {Fore.LIGHTYELLOW_EX}Thunder,{Style.RESET_ALL} {Fore.MAGENTA}'e'{Style.RESET_ALL} for {Fore.MAGENTA}Earth,{Style.RESET_ALL} or {Fore.MAGENTA}'wi'{Style.RESET_ALL} for {Fore.LIGHTGREEN_EX}Wind.{Style.RESET_ALL}").lower()
      if choice == 'a':
        self.attack_lvl += 1
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} is now {Fore.CYAN}attack level {self.attack_lvl}!{Style.RESET_ALL}")
      elif choice == 'd':
        self.defense_lvl += 1
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} is now {Fore.CYAN}defense level {self.defense_lvl}!{Style.RESET_ALL}")
      elif choice == 'f':
        self.axe_element("Fire")
      elif choice == 'i':
        self.axe_element("Ice")
      elif choice == 'wa':
        self.axe_element("Water")
      elif choice == 't':
        self.axe_element("Thunder")
      elif choice == 'e':
        self.axe_element("Earth")
      elif choice == 'wi':
        self.axe_element("Wind")
    else:
      if self.axe == False:
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has leveled up! {Fore.CYAN}{self.name}{Style.RESET_ALL} is now {Fore.CYAN}level {self.level}{Style.RESET_ALL}.")
        choice = input(f"You may level up an attribute. Press {Fore.MAGENTA}'a'{Style.RESET_ALL} to boost attack or{Fore.MAGENTA}'d'{Style.RESET_ALL} to boost defense.").lower()
        while choice not in level_choice:
          choice = input(f"Sorry, that is not an option. Press {Fore.MAGENTA}'a'{Style.RESET_ALL} to boost attack or{Fore.MAGENTA}'d'{Style.RESET_ALL} to boost defense.").lower()
        if choice == 'a':
          self.attack_lvl += 1
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} is now {Fore.CYAN}attack level {self.attack_lvl}!{Style.RESET_ALL}")
        elif choice == 'd':
          self.defense_lvl += 1
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} is now {Fore.CYAN}defense level {self.defense_lvl}!{Style.RESET_ALL}")




  def death(self):
    # When a character's health is reduced to 0, the is_dead status will flip to True, the character will die and the game ends.
    self.is_dead = True
    prRed("""  
               Y   Y  OOO  U   U    DDDD  IIIII EEEEE DDDD 
                Y Y  O   O U   U    D   D   I   E     D   D
                 Y   O   O U   U    D   D   I   EEE   D   D
                 Y   O   O U   U    D   D   I   E     D   D
                 Y    OOO   UUU     DDDD  IIIII EEEEE DDDD  """)
    if foyer_case_knife == False:
      prRed(f"\nWhat a cheap way to go. These game developers are some punks.")
    quit()

  def flee(self):
  # Generates a random number and gives the player a 25% chance of escaping the battle
    if random.randint(1,4) == 1:
      self.flee_chance = True
      prYellow("""
      
               Y   Y  OOO  U   U    RRRR    A   N   N
                Y Y  O   O U   U    R   R  A A  NN  N
                 Y   O   O U   U    RRRR  AAAAA N N N   
                 Y   O   O U   U    R  R  A   A N  NN
                 Y    OOO   UUU     R   R A   A N   N   
                 
                    """)
      time.sleep(2) 

    else:
      prYellow("""You tripped on a rock!""")

  def make_friends(self):
    #Easter egg, secret option to end the game with some dialogue.
    os.system('clear||cls')  
    prGreen("""You ask the Jelly how it is doing today. 
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

    input("Press 'Enter' to exit.")
    quit() 

  def spare_sleepy_jelly(self):
    global spare_counter
    spare_list = ['yes', 'no']
    choice = input(f"You wonder if killing this {Fore.LIGHTGREEN_EX}Jelly{Style.RESET_ALL} is the right thing to do.\nWill you spare the {Fore.LIGHTGREEN_EX}Jelly?{Style.RESET_ALL} Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    while choice not in spare_list: 
          choice = input(f"Sorry, that is not an available option. Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()  
    if choice == 'yes':
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has spared the {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly{Style.RESET_ALL} drops the {Fore.LIGHTYELLOW_EX}Sleepy Bundle.{Style.RESET_ALL}\n{Fore.CYAN}{self.name} gains two {Fore.LIGHTYELLOW_EX}potions{Style.RESET_ALL} and the {Fore.CYAN}Axe of Preserves!{Style.RESET_ALL}")
          time.sleep(1)
          self.potions += 2
          self.axe = True 
          list_of_ele_choices = ['f', 'i' , 'wa', 't', 'wi', 'e']
          element_choice = input(f"The axe speaks to your mind. It says, \"What element would you like me to be?\"\nPlease choose an element.\n Press {Fore.MAGENTA}'f'{Style.RESET_ALL} for Fire, {Fore.MAGENTA}'i'{Style.RESET_ALL} for Ice, {Fore.MAGENTA}'wa'{Style.RESET_ALL} for Water, {Fore.MAGENTA}'t'{Style.RESET_ALL} for Thunder, {Fore.MAGENTA}'wi'{Style.RESET_ALL} for Wind, or {Fore.MAGENTA}'e'{Style.RESET_ALL} for Earth.").lower()
          while element_choice not in list_of_ele_choices:
            element_choice = input(f"Sorry, that is not an available option.\nPress {Fore.MAGENTA}'f'{Style.RESET_ALL} for Fire, {Fore.MAGENTA}'i'{Style.RESET_ALL} for Ice, {Fore.MAGENTA}'wa'{Style.RESET_ALL} for Water, {Fore.MAGENTA}'t'{Style.RESET_ALL} for Thunder, {Fore.MAGENTA}'wi'{Style.RESET_ALL} for Wind, or {Fore.MAGENTA}'e'{Style.RESET_ALL} for Earth.").lower()    
          if element_choice == 'f':
            self.axe_element("Fire")
            print(f"You have added the {Fore.LIGHTRED_EX}Fire{Style.RESET_ALL} element to the Axe.")
            time.sleep(1)
          elif element_choice == 'i':
            self.axe_element("Ice")
            print(f"You have added the {Fore.CYAN}Ice{Style.RESET_ALL} element to the Axe.")
            time.sleep(1)
          elif element_choice == 'wa':
            self.axe_element("Water")
            print(f"You have added the {Fore.CYAN}Water{Style.RESET_ALL} element to the Axe.")
            time.sleep(1)
          elif element_choice == 't':
            self.axe_element("Thunder")
            print(f"You have added the {Fore.LIGHTYELLOW_EX}Thunder{Style.RESET_ALL} element to the Axe.")
            time.sleep(1)
          elif element_choice == 'wi':
            self.axe_element("Wind")
            print(f"You have added the {Fore.LIGHTGREEN_EX}Wind{Style.RESET_ALL} element to the Axe.")
            time.sleep(1)
          elif element_choice == 'e':
            self.axe_element("Earth")
            print(f"You have added the {Fore.MAGENTA}Earth{Style.RESET_ALL} element to the Axe.")
          jelly_1.victory()
    elif choice == 'no':
          print(f"{Fore.CYAN}{self.name} has decided not to spare the {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL} Carry on.")
          spare_counter = 0
    
  def lose_health(self, amount):
  # Deducts health from a character and prints the health remaining. If player is wearing ring, damage is reduced by 1/3.
    if self.defense_lvl == 1:
      self.health -= amount 
    elif self.defense_lvl == 2:
      self.health -= round(amount // 1.1) 
    elif self.defense_lvl == 3:
      self.health -= round(amount // 1.2)
    elif self.defense_lvl == 4:
      self.health -= round(amount // 1.3)
    elif self.defense_lvl == 5:
      self.health -= round(amount // 1.4) 
    elif self.defense_lvl == 6:
      self.health -= round(amount // 1.5)
    elif self.defense_lvl == 7:
      self.health -= round(amount // 1.6)
    elif self.defense_lvl == 8:
      self.health -= round(amount // 1.7)
    elif self.defense_lvl == 9:
      self.health -= round(amount // 1.8) 
    elif self.defense_lvl == 10:
      self.health -= round(amount // 1.9)
    elif self.defense_lvl == 11:
      self.health -= round(amount // 2)
    if self.health <= 0:
      self.death()
    else:
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has {Fore.YELLOW}{self.health} HP{Style.RESET_ALL} remaining. {Fore.CYAN}{self.name}{Style.RESET_ALL} has {Fore.YELLOW}{self.potions} potions{Style.RESET_ALL} remaining.")
  
  def attack(self, enemy):
  # Selects a random number from range 1-6 and if 1, attack will miss the jelly. Otherwise, selects a random number from range 5-15 and uses the value in the lose_health function. If player has sword then damage increases by 1.5. Each attack level increases attack by 10 percent.
    miss = 1
    if random.randint(1,7) == miss:                                      
      damage = 0
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} misses the {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL}!")
    else:
      if self.sword == True:
        if self.attack_lvl == 1:
          damage = round(random.randint(5,15) * 1.5)
        elif self.attack_lvl == 2:
          damage = round(random.randint(5,15) * 1.6)
        elif self.attack_lvl == 3:
          damage = round(random.randint(5,15) * 1.7)
        elif self.attack_lvl == 4:
          damage = round(random.randint(5,15) * 1.8)
        elif self.attack_lvl == 5:
          damage = round(random.randint(5,15) * 1.9)
        elif self.attack_lvl == 6:
          damage = round(random.randint(5,15) * 2)
        elif self.attack_lvl == 7:
          damage = round(random.randint(5,15) * 2.1)
        elif self.attack_lvl == 8:
          damage = round(random.randint(5,15) * 2.2)
        elif self.attack_lvl == 9:
          damage = round(random.randint(5,15) * 2.3)
        elif self.attack_lvl == 10:
          damage = round(random.randint(5,15) * 2.4)
        elif self.attack_lvl == 11:
          damage = round(random.randint(5,15) * 2.5)
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses the {Fore.CYAN}Butterknife of Truth!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.RED}{damage} HP damage.{Style.RESET_ALL}")
        enemy.lose_health(damage)
      else:
        if self.attack_lvl == 1:
          damage = random.randint(5,15)
        elif self.attack_lvl == 2:
          damage = round(random.randint(5,15) * 1.1)
        elif self.attack_lvl == 3:
          damage = round(random.randint(5,15) * 1.2)
        elif self.attack_lvl == 4:
          damage = round(random.randint(5,15) * 1.3)
        elif self.attack_lvl == 5:
          damage = round(random.randint(5,15) * 1.9)
        elif self.attack_lvl == 6:
          damage = round(random.randint(5,15) * 2)
        elif self.attack_lvl == 7:
          damage = round(random.randint(5,15) * 2.1)
        elif self.attack_lvl == 8:
          damage = round(random.randint(5,15) * 2.2)
        elif self.attack_lvl == 9:
          damage = round(random.randint(5,15) * 2.3)
        elif self.attack_lvl == 10:
          damage = round(random.randint(5,15) * 2.4)
        elif self.attack_lvl == 11:
          damage = round(random.randint(5,15) * 2.5)
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} attacks the {Fore.LIGHTGREEN_EX}{enemy.element} Jelly!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.RED}{damage} HP damage.{Style.RESET_ALL}")
        enemy.lose_health(damage)

  def champ_player_attack(self, enemy):
  # Selects a random number from range 1-6 and if 1, attack will miss the jelly. Otherwise, selects a random number from range 5-15 and uses the value in the lose_health function. If player has sword then damage increases by 1.5. Each attack level increases attack by 10 percent.
    miss = 1
    if random.randint(1,7) == miss:                                      
      damage = 0
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} misses the {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL}!")
    else:
      if self.sword == True:
        if self.attack_lvl == 1:
          damage = round(random.randint(5,15) * 1.5)
        elif self.attack_lvl == 2:
          damage = round(random.randint(5,15) * 1.6)
        elif self.attack_lvl == 3:
          damage = round(random.randint(5,15) * 1.7)
        elif self.attack_lvl == 4:
          damage = round(random.randint(5,15) * 1.8)
        elif self.attack_lvl == 5:
          damage = round(random.randint(5,15) * 1.9)
        elif self.attack_lvl == 6:
          damage = round(random.randint(5,15) * 2)
        elif self.attack_lvl == 7:
          damage = round(random.randint(5,15) * 2.1)
        elif self.attack_lvl == 8:
          damage = round(random.randint(5,15) * 2.2)
        elif self.attack_lvl == 9:
          damage = round(random.randint(5,15) * 2.3)
        elif self.attack_lvl == 10:
          damage = round(random.randint(5,15) * 2.4)
        elif self.attack_lvl == 11:
          damage = round(random.randint(5,15) * 2.5)
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses the {Fore.CYAN}Butterknife of Truth!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.RED}{damage} HP damage.{Style.RESET_ALL}")
        enemy.lose_health_champ(damage)
      else:
        if self.attack_lvl == 1:
          damage = random.randint(5,15)
        elif self.attack_lvl == 2:
          damage = round(random.randint(5,15) * 1.1)
        elif self.attack_lvl == 3:
          damage = round(random.randint(5,15) * 1.2)
        elif self.attack_lvl == 4:
          damage = round(random.randint(5,15) * 1.3)
        elif self.attack_lvl == 5:
          damage = round(random.randint(5,15) * 1.9)
        elif self.attack_lvl == 6:
          damage = round(random.randint(5,15) * 2)
        elif self.attack_lvl == 7:
          damage = round(random.randint(5,15) * 2.1)
        elif self.attack_lvl == 8:
          damage = round(random.randint(5,15) * 2.2)
        elif self.attack_lvl == 9:
          damage = round(random.randint(5,15) * 2.3)
        elif self.attack_lvl == 10:
          damage = round(random.randint(5,15) * 2.4)
        elif self.attack_lvl == 11:
          damage = round(random.randint(5,15) * 2.5)
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} attacks the {Fore.LIGHTGREEN_EX}Jelly King's Champion!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.RED}{damage} HP damage.{Style.RESET_ALL}")
        enemy.lose_health_champ(damage)

  def axe_element(self, axe_element):
    #Elemental Weaknesses(strong-->weak) Fire-->Ice, Ice-->Water, Water-->Fire
    #Thunder-->Wind, Wind-->Earth, Earth-->Thunder
    global player_axe_elements
    list_of_axe_elements = ["Earth", "Fire", "Ice", "Thunder", "Water", "Wind"]
    if axe_element in player_axe_elements:
      print("You already have that element. Please choose a different element.")
      player_1.level_up()
    
    elif axe_element == 'Fire': print(f"{self.name} has added the {Fore.LIGHTRED_EX}'Fire'{Style.RESET_ALL} element to the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
    elif axe_element == 'Ice': print(f"{self.name} has added the {Fore.CYAN}'Ice'{Style.RESET_ALL} element to the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
    elif axe_element == 'Water': print(f"{self.name} has added the {Fore.CYAN}'Water'{Style.RESET_ALL} element to the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
    elif axe_element == 'Thunder': print(f"{self.name} has added the {Fore.LIGHTYELLOW_EX}'Thunder'{Style.RESET_ALL} element to the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}") 
    elif axe_element == 'Wind': print(f"{self.name} has added the {Fore.LIGHTGREEN_EX}'Wind'{Style.RESET_ALL} element to the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
    elif axe_element == 'Earth': print(f"{self.name} has added the {Fore.MAGENTA}'Earth'{Style.RESET_ALL} element to the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
    player_axe_elements.append(axe_element)
      
    
  
  def elemental_attack(self, enemy):
    global player_axe_elements
    choice_list = []
    for element in player_axe_elements:
      choice_list.append(element)
    print(f"Which element will you charge the {Fore.CYAN}Axe of Preserves{Style.RESET_ALL} with?\nType from your collected elements:")
    choice = input(choice_list   ).title() 
    while choice not in choice_list:
      print(f"Sorry, that's not an available option. Please type from your collected elements:")
      choice = input(choice_list   ).title() 
    if choice == 'Fire':
      if enemy.element == 'Ice':
        damage = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
      elif enemy.element == 'Fire':
        gain_health = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
        enemy.health += 30 
      else:
        damage = 15
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
    if choice == 'Ice':
      if enemy.element == 'Water':
        damage = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
      elif enemy.element == 'Ice':
        gain_health = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
        enemy.health += 30 
      else:
        damage = 15
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
    if choice == 'Water':
      if enemy.element == 'Fire':
        damage = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
      elif enemy.element == 'Water':
        gain_health = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
        enemy.health += 30 
      else:
        damage = 15
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
    if choice == 'Thunder':
      if enemy.element == 'Wind':
        damage = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
      elif enemy.element == 'Thunder':
        gain_health = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
        enemy.health += 30 
      else:
        damage = 15
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
    if choice == 'Wind':
      if enemy.element == 'Earth':
        damage = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
      elif enemy.element == 'Wind':
        gain_health = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
        enemy.health += 30 
      else:
        damage = 15
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
    if choice == 'Earth':
      if enemy.element == 'Thunder':
        damage = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.MAGENTA}Earth Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)
      elif enemy.element == 'Earth':
        gain_health = 30
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.MAGENTA}Earth Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
        enemy.health += 30 
      else:
        damage = 15
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses Earth Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}{enemy.element} Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
        enemy.lose_health(damage)

  def champ_elemental_attack(self, enemy):
    global meditation_active  
    global player_axe_elements
    choice_list = []
    damage = 0
    for element in player_axe_elements:
      choice_list.append(element)
    print(f"Which element will you charge the {Fore.CYAN}Axe of Preserves{Style.RESET_ALL} with?\nType from your collected elements:")
    choice = input(choice_list   ).title() 
    while choice not in choice_list:
      print(f"Sorry, that's not an available option. Please type from your collected elements:")
      choice = input(choice_list   ).title() 
    if meditation_active:
      damage += 30
      if choice == 'Fire':
        if enemy.element == 'Ice':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Fire':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion Jelly{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Ice':
        if enemy.element == 'Water':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Ice':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Water':
        if enemy.element == 'Fire':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Water':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Thunder':
        if enemy.element == 'Wind':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Thunder':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Wind':
        if enemy.element == 'Earth':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Wind':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Earth':
        if enemy.element == 'Thunder':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.MAGENTA}Earth Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Earth':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.MAGENTA}Earth Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses Earth Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
    else:
      if choice == 'Fire':
        if enemy.element == 'Ice':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Fire':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion Jelly{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTRED_EX}Fire Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Ice':
        if enemy.element == 'Water':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Ice':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Ice Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Water':
        if enemy.element == 'Fire':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Water':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.CYAN}Water Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Thunder':
        if enemy.element == 'Wind':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Thunder':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.YELLOW}Thunder Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Wind':
        if enemy.element == 'Earth':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Wind':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Wind Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
      if choice == 'Earth':
        if enemy.element == 'Thunder':
          damage += 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.MAGENTA}Earth Attack!{Style.RESET_ALL} It's extremely effective. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
        elif enemy.element == 'Earth':
          gain_health = 30
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses {Fore.MAGENTA}Earth Attack!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} absorbs {Fore.YELLOW}{gain_health} HP{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL} Woops.")
          enemy.health += 30 
        else:
          damage += 15
          print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses Earth Attack!{Style.RESET_ALL} It's meh. The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage{Style.RESET_ALL}\nfrom the {Fore.CYAN}Axe of Preserves.{Style.RESET_ALL}")
          enemy.lose_health_champ(damage)
  
  def use_potion(self):
    if self.potions > 0:
      self.health += 30
      self.potions -= 1
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses a {Fore.YELLOW}potion!{Style.RESET_ALL} {Fore.CYAN}{self.name}'s{Style.RESET_ALL} {Fore.YELLOW}HP{Style.RESET_ALL} increases by {Fore.YELLOW}30.{Style.RESET_ALL}\n{Fore.CYAN}{self.name}{Style.RESET_ALL} has {Fore.YELLOW}{self.health} HP{Style.RESET_ALL} remaining.")
      time.sleep(0.5)
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has {Fore.YELLOW}{self.potions} potions{Style.RESET_ALL} remaining.")
    elif self.potions == 0:
      print(f"You reach for a {Fore.YELLOW}potion{Style.RESET_ALL}, but your bag is {Fore.YELLOW}empty!{Style.RESET_ALL}")

  def use_potion_ally(self, ally):
    if self.potions > 0:
      ally.health += 30
      self.potions -= 1
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses a {Fore.YELLOW}potion{Style.RESET_ALL} on {Fore.CYAN}{ally.name}! {ally.name}'s{Style.RESET_ALL} {Fore.YELLOW}HP{Style.RESET_ALL} increases by {Fore.YELLOW}30.{Style.RESET_ALL}\n{Fore.CYAN}{ally.name}{Style.RESET_ALL} has {Fore.YELLOW}{ally.health} HP{Style.RESET_ALL} remaining.")
      time.sleep(0.5)
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has {Fore.YELLOW}{self.potions} potions{Style.RESET_ALL} remaining.")
    elif self.potions == 0:
      print(f"You reach for a {Fore.YELLOW}potion{Style.RESET_ALL}, but your bag is {Fore.YELLOW}empty!{Style.RESET_ALL}")
   

      
class Jelly:
# The Jelly instances are automatically created upon program initiation.
  def __init__(self, spell=False, element=None, health = 40):
    self.health = health
    self.spell = spell 
    self.element = element
    self.is_dead = False
  
  def __repr__(self):
    # Printing a jelly will tell you how much health the jelly has left.
    return "The Jelly has {health} HP remaining.".format(health = self.health)

  def select_fake_element(self):
    list_of_fake_elements = ["Strawberry", "Grape", "Ubiquitous", "Peanut Butter"]
    self.element = random.choice(list_of_fake_elements)

  def sleepy_element(self, element="Sleepy"):
    self.element = element

  def chef_element(self, element="Chef"):
    self.element = element

  def chef_attack(self, player):
    list_of_attacks = ["Fine Cutlery", "Rolling Pin", "Sautee", "Chef's Knife"]
    damage = 10 
    print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}{random.choice(list_of_attacks)}. {Style.RESET_ALL}{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
    player.lose_health(damage)

  def fart_attack(self, player):
    list_of_attacks = ["Wet Kiss", "High Fiber", "Irratable Bowel Syndrome", "Colon Cleanse"]
    attack_choice = random.choice(list_of_attacks)
    damage = random.randint(15,25)
    print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}{attack_choice}. {Style.RESET_ALL}{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
    player.lose_health(damage)
  
  def sbd_attack(self, player):
    damage = random.randint(5,10)
    print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}Silent but Deadly.{Style.RESET_ALL} You don't hear anything, but you're {Fore.LIGHTGREEN_EX}POISONED. {Style.RESET_ALL}{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
    player.is_poisoned = True
    player.lose_health(damage)

  def bake_cake(self, player):
    global cake_counter
    global eat_cake 
    print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}'Will you try my cake and delicious Jelly milk?'{Style.RESET_ALL}")
    choice_list = ['yes', 'no']
    choice = input(f"Will you try {Fore.LIGHTGREEN_EX}Chef Jelly's cake and delicious Jelly milk?{Style.RESET_ALL} Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}")
    while choice not in choice_list:
      choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}")
    if choice == 'yes':
      eat_cake = True 
      player_1.health += 60
      player_1.xp += 20 
      print(f"This {Fore.LIGHTGREEN_EX}cake{Style.RESET_ALL} is delicious! You wash it down with the rich and smooth {Fore.LIGHTGREEN_EX}Jelly milk.{Style.RESET_ALL}\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} gains {Fore.YELLOW}60 HP{Style.RESET_ALL} and {Fore.YELLOW}20 experience points.{Style.RESET_ALL}")
      time.sleep(1)
      jelly_1.victory()
    elif choice == 'no':
      print(f"You have decided not to eat the {Fore.LIGHTGREEN_EX}Cake{Style.RESET_ALL} or drink the {Fore.LIGHTGREEN_EX}milk.{Style.RESET_ALL}\nAre you Lactose intolerant or something?")
      cake_counter = 0

  def spell_enable(self, spell=False):
    self.spell = True 



  def sleepy_attack(self, player):
    list_of_attacks = ["Narcolepsy", "Doze Off", "Nod Off", "Decaf Coffee", "I Just Worked Two Doubles"]
    print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}{random.choice(list_of_attacks)}.{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} is asleep.")

  def select_element(self, element=None):
    list_of_elements = ["Fire", "Ice", "Water", "Thunder", "Wind", "Earth"]
    self.element = element

  def lose_health(self, amount):
  # Deducts health from a jelly and prints the health remaining
    self.health -= amount
    if self.health <= 0:
      self.victory()
    else:
      print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} has {Fore.YELLOW}{self.health} HP{Style.RESET_ALL} remaining.")
  
  def reset_health(self, amount=40):
    self.health = amount 

  def attack(self, player):
  # Selects a random number from range 5-15 and uses the value in the lose_health function. Adds an additional amount of damage if jelly element is Earth, Wind, Fire, Water, Thunder, or Ice.
    if self.spell == True:
      spell_chance = random.randint(1,4)
      if spell_chance == 1:
        print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}'{self.element}'.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}30 HP damage.{Style.RESET_ALL}")
        damage = 30
        player.lose_health(damage)
      else:
          if player_1.boots == True:
            if random.randint(1,3) == 1:
              damage = 0
              print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL} Your feet feel so light.")
            else:
              if player.ring == True:
                prCyan("The Ring of Defense has Activated!")  
                damage = round(random.randint(5,15) / 1.5)
                damage_elements = ["Fire", "Water", "Wind", "Earth", "Thunder", "Ice"] 
                print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                if self.element in damage_elements:
                    elemental_damage = round(random.randint(1, 5) / 1.5) 
                    damage += elemental_damage
                    print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                    player.lose_health(damage)
                else:
                    player.lose_health(damage)
              elif player.ring == False:
                damage = random.randint(5,15)
                damage_elements = ["Fire", "Water", "Wind", "Earth", "Thunder", "Ice"] 
                print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                if self.element in damage_elements:
                    elemental_damage = random.randint(1, 5) 
                    damage += elemental_damage
                    print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                    player.lose_health(damage)
                else:
                    player.lose_health(damage)

          elif player_1.boots == False:  
            if random.randint(1,6) == 1:
              damage = 0
              print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL}")
            else:
              if player.ring == True:
                prCyan("The Ring of Defense has Activated!")  
                damage = round(random.randint(5,15) / 1.5)
                damage_elements = ["Fire", "Water", "Wind", "Earth", "Thunder", "Ice"] 
                print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                if self.element in damage_elements:
                    elemental_damage = round(random.randint(1, 5) / 1.5) 
                    damage += elemental_damage
                    print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                    player.lose_health(damage)
                else:
                    player.lose_health(damage)
              elif player.ring == False:
                damage = random.randint(5,15)
                damage_elements = ["Fire", "Water", "Wind", "Earth", "Thunder", "Ice"] 
                print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                if self.element in damage_elements:
                    elemental_damage = random.randint(1, 5) 
                    damage += elemental_damage
                    print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                    player.lose_health(damage)
                else:
                    player.lose_health(damage)
    elif self.spell == False:
      if player_1.boots == True:
            if random.randint(1,3) == 1:
              damage = 0
              print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL} Your feet feel so light.")
            else:
              if player.ring == True:
                prCyan("The Ring of Defense has Activated!")  
                damage = round(random.randint(5,15) / 1.5)
                damage_elements = ["Fire", "Water", "Wind", "Earth", "Thunder", "Ice"] 
                print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                if self.element in damage_elements:
                    elemental_damage = round(random.randint(1, 5) / 1.5) 
                    damage += elemental_damage
                    print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                    player.lose_health(damage)
                else:
                    player.lose_health(damage)
              elif player.ring == False:
                damage = random.randint(5,15)
                damage_elements = ["Fire", "Water", "Wind", "Earth", "Thunder", "Ice"] 
                print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                if self.element in damage_elements:
                    elemental_damage = random.randint(1, 5) 
                    damage += elemental_damage
                    print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                    player.lose_health(damage)
                else:
                    player.lose_health(damage)

      elif player_1.boots == False:  
            if random.randint(1,6) == 1:
              damage = 0
              print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL}")
            else:
              if player.ring == True:
                prCyan("The Ring of Defense has Activated!")  
                damage = round(random.randint(5,15) / 1.5)
                damage_elements = ["Fire", "Water", "Wind", "Earth", "Thunder", "Ice"] 
                print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                if self.element in damage_elements:
                    elemental_damage = round(random.randint(1, 5) / 1.5) 
                    damage += elemental_damage
                    print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                    player.lose_health(damage)
                else:
                    player.lose_health(damage)
              elif player.ring == False:
                damage = random.randint(5,15)
                damage_elements = ["Fire", "Water", "Wind", "Earth", "Thunder", "Ice"] 
                print(f"The {Fore.LIGHTGREEN_EX}{self.element} Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                if self.element in damage_elements:
                    elemental_damage = random.randint(1, 5) 
                    damage += elemental_damage
                    print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                    player.lose_health(damage)
                else:
                    player.lose_health(damage)

  def victory(self):
  # If player defeats the Jelly, they get a victory message and 10 xp points.
    global eat_cake
    time.sleep(1)
    print(f"\nThe {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly{Style.RESET_ALL} has been defeated.")
    
    prGreen("""
             Y   Y  OOO  U   U    W   W IIIII N   N
              Y Y  O   O U   U    W   W   I   NN  N
               Y   O   O U   U    W W W   I   N N N
               Y   O   O U   U    WW WW   I   N  NN
               Y    OOO   UUU     W   W IIIII N   N  
               """)

    if eat_cake == True:
      print("Actually, everyone wins when there is cake involved.")

    time.sleep(1)
    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} has {Fore.YELLOW}{player_1.health} HP{Style.RESET_ALL} remaining.")
    player_1.gain_xp(10)
    input(f"Press {Fore.LIGHTMAGENTA_EX}'Enter'{Style.RESET_ALL} to continue...")
     
    os.system('clear||cls')

class HeroJelly:
# Used in final battle if Hero Jelly sidequest is completed
  def __init__(self, name, health=100, potions=3, is_dead=False):
    self.name = name
    self.health = health
    self.potions = potions
    self.is_dead = is_dead 

  def attack(self, enemy, ally):
    miss_and_potion = 1
    if random.randint(1,4) == miss_and_potion:
      self.use_potion(ally)
    else:
      if random.randint(1,6) == miss_and_potion:                                      
        damage = 0
        print(f"{Fore.CYAN}The Great Hero Jelly{Style.RESET_ALL} misses the {Fore.GREEN}Ancient Jelly!{Style.RESET_ALL}")
      else:
        damage = random.randint(10,20)
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} attacks the {Fore.GREEN}Ancient Jelly!{Style.RESET_ALL} The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
        enemy.lose_health(damage)

  def champ_player_attack(self, enemy, ally):
    miss_and_potion = 1
    if random.randint(1,4) == miss_and_potion:
      self.use_potion(ally)
    else:
      if random.randint(1,6) == miss_and_potion:                                      
        damage = 0
        print(f"{Fore.CYAN}The Great Hero Jelly{Style.RESET_ALL} misses the {Fore.GREEN}Jelly King's Champion!{Style.RESET_ALL}")
      else:
        damage = random.randint(10,20)
        print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} attacks the {Fore.GREEN}Jelly King's Champion!{Style.RESET_ALL} The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
        enemy.lose_health_champ(damage)

  
  
  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.is_dead = True
      time.sleep(2) 
      print(f"WHAT A TRAGIC TURN OF EVENTS, {Fore.CYAN}THE GREAT HERO JELLY{Style.RESET_ALL} HAS DIED!")
      time.sleep(2)
    else:
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has {Fore.YELLOW}{self.health} HP{Style.RESET_ALL} remaining.")
  
  def use_potion(self, ally):
    if self.potions > 0:
      ally.health += 30
      self.potions -= 1
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} uses a {Fore.YELLOW}potion!{Style.RESET_ALL} {Fore.CYAN}{ally.name}'s{Style.RESET_ALL}{Fore.YELLOW} HP{Style.RESET_ALL} increases by {Fore.YELLOW}30.{Style.RESET_ALL}\n{Fore.CYAN}{ally.name}{Style.RESET_ALL} has {Fore.YELLOW}{ally.health} HP{Style.RESET_ALL} remaining.")
      time.sleep(0.5)
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} has {Fore.YELLOW}{self.potions} potions{Style.RESET_ALL} remaining.")
    elif self.potions == 0:
      print(f"{Fore.CYAN}{self.name}{Style.RESET_ALL} reaches for a {Fore.YELLOW}potion{Style.RESET_ALL}, but it's bag is {Fore.YELLOW}empty!{Style.RESET_ALL}")

class BossJelly:
  def __init__(self, health=200, spell=False, potions=1, element="Ancient"):
    self.health = health
    self.spell = spell
    self.potions = potions 
    self.element = element 
  
  # Ancient Jelly methods
  
  def use_ancient_potion(self):
    self.potions -= 1
    self.health += 30
    print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} uses a {Fore.YELLOW}potion.{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} gains {Fore.YELLOW}30 HP.{Style.RESET_ALL}")
    time.sleep(1)
    print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} has {Fore.YELLOW}{boss_jelly.health} HP{Style.RESET_ALL} remaining.")
  
  def attack(self, player, hero):
    if player_1.ally == True and hero.is_dead == False:
      player_attack = ['player', 'hero']
      if random.choice(player_attack) == 'player': 
        if player_1.boots == True:
          if random.randint(1,3) == 1:
            damage = 0
            print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL} Your feet feel so light.")
          else:
            if player.ring == True:
              prCyan("The Ring of Defense has Activated!")  
              damage = round(random.randint(20, 30) / 1.5)
              print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
              player.lose_health(damage)
            elif player.ring == False:
              damage = random.randint(20, 30)
              print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
              player.lose_health(damage)

        elif player_1.boots == False:  
          if random.randint(1,6) == 1:
            damage = 0
            print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL}")
          else:
            if player.ring == True:
              prCyan("The Ring of Defense has Activated!")  
              damage = round(random.randint(20, 30) / 1.5)
              print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
              player.lose_health(damage)
            elif player.ring == False:
              damage = random.randint(20, 30)
              print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
              player.lose_health(damage)
      elif random.choice(player_attack) == 'hero':
        if random.randint(1,6) == 1:
            damage = 0
            print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} misses {Fore.CYAN}{hero.name}!{Style.RESET_ALL}")
        else:
          damage = random.randint(20, 30)
          print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          hero.lose_health(damage)
    elif player_1.ally == False or hero.is_dead == True:
      if player_1.boots == True:
          if random.randint(1,3) == 1:
            damage = 0
            print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL} Your feet feel so light.")
          else:
            if player.ring == True:
              prCyan("The Ring of Defense has Activated!")  
              damage = round(random.randint(20, 30) / 1.5)
              print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
              player.lose_health(damage)
            elif player.ring == False:
              damage = random.randint(20, 30)
              print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
              player.lose_health(damage)

      elif player_1.boots == False:  
          if random.randint(1,6) == 1:
            damage = 0
            print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL}")
          else:
            if player.ring == True:
              prCyan("The Ring of Defense has Activated!")  
              damage = round(random.randint(20, 30) / 1.5)
              print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
              player.lose_health(damage)
            elif player.ring == False:
              damage = random.randint(20, 30)
              print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
              player.lose_health(damage)

  def millenium_reminisce(self, player, hero):
    list_of_attacks = ['Millenium', 'Reminisce']
    if player.ally == True and hero.is_dead == False:
      list_of_players = ['player', 'hero']
      if random.choice(list_of_players) == 'player':
        if random.choice(list_of_attacks) == 'Millenium':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} uses {Fore.GREEN}Millenium.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"An attack for the ages!!!\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
        else:
          damage = random.randint(30, 40)
          print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} uses {Fore.GREEN}Reminisce.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Ouch!!! They sure don't make em' like they used to.\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
      elif random.choice(list_of_players) == 'hero':
        if random.choice(list_of_attacks) == 'Millenium':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} uses {Fore.GREEN}Millenium.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"An attack for the ages!!!\n{Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          hero.lose_health(damage)
        else:
          damage = random.randint(30, 40)
          print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} uses {Fore.GREEN}Reminisce.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Ouch!!! They sure don't make em' like they used to.\n{Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          hero.lose_health(damage)
    elif player.ally == False or hero.is_dead == True:
      if random.choice(list_of_attacks) == 'Millenium':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} uses {Fore.GREEN}Millenium.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"An attack for the ages!!!\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
      else:
          damage = random.randint(30, 40)
          print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} uses {Fore.GREEN}Reminisce.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Ouch!!! They sure don't make em' like they used to.\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)

  def celestial_doom(self, player, hero):
    damage = 100
    if player.ally == True and hero.is_dead == False:
      list_of_players = ['player', 'hero']
      if random.choice(list_of_players) == 'player':
        print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} casts {Fore.GREEN}Celestial Doom.{Style.RESET_ALL}")
        time.sleep(2)
        print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
        player.lose_health(damage)
        self.ancient_defeat()
      elif random.choice(list_of_players) == 'hero':
        print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} casts {Fore.GREEN}Celestial Doom.{Style.RESET_ALL}")
        time.sleep(2)
        print(f"{Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
        hero.lose_health(damage)
        self.ancient_defeat()
    elif player.ally == False or hero.is_dead == True:
        print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} casts {Fore.GREEN}Celestial Doom.{Style.RESET_ALL}")
        time.sleep(2)
        print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
        player.lose_health(damage)
        self.ancient_defeat()

  # Jelly King's Champion methods

  def select_champ_element(self):
    list_of_elements = ["Fire", "Ice", "Water", "Thunder", "Wind", "Earth"]
    element = random.choice(list_of_elements)
    self.element = element

  def use_potion(self):
    self.potions -= 1
    self.health += 30
    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} uses a {Fore.YELLOW}potion.{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} gains {Fore.YELLOW}30 HP.{Style.RESET_ALL}")
    time.sleep(1)
    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} has {Fore.YELLOW}{champ_jelly.health} HP{Style.RESET_ALL} remaining.")
  
  def list_of_champion_attacks(self, player, hero):
    list_of_attacks = ['Eviscerate', 'Blade of the King', 'Advanced Technique', 'Meditate']
    if player.ally == True and hero.is_dead == False:
      list_of_players = ['player', 'hero']
      if random.choice(list_of_players) == 'player':
        if random.choice(list_of_attacks) == 'Eviscerate':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Eviscerate.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"You feel empty inside!!!\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
        elif random.choice(list_of_attacks) == 'Blade of the King':
          damage = random.randint(30, 40)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Blade of the King.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Feel the justice so swift!\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
        elif random.choice(list_of_attacks) == 'Advanced Technique':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Advanced Technique.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Truly a master of his craft!!!\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
        elif random.choice(list_of_attacks) == 'Meditate':
          self.meditation()
      elif random.choice(list_of_players) == 'hero':
        if random.choice(list_of_attacks) == 'Eviscerate':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Eviscerate.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"The Hero feels empty inside!!!\n{Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          hero.lose_health(damage)
        elif random.choice(list_of_attacks) == 'Blade of the King':
          damage = random.randint(30, 40)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Blade of the King.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Feel the justice so swift!\n{Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          hero.lose_health(damage)
        elif random.choice(list_of_attacks) == 'Advanced Technique':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Advanced Technique.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Truly a master of his craft!!!\n{Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          hero.lose_health(damage)
        elif random.choice(list_of_attacks) == 'Meditate':
          self.meditation()
    elif player.ally == False or hero.is_dead == True:
      if random.choice(list_of_attacks) == 'Eviscerate':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Eviscerate.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"You feel empty inside!!!\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
      elif random.choice(list_of_attacks) == 'Blade of the King':
          damage = random.randint(30, 40)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Blade of the King.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Feel the justice so swift!\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
      elif random.choice(list_of_attacks) == 'Advanced Technique':
          damage = random.randint(40, 50)
          print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Advanced Technique.{Style.RESET_ALL}")
          time.sleep(2)
          print(f"Truly a master of his craft!!!\n{Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
          player.lose_health(damage)
      elif random.choice(list_of_attacks) == 'Meditate':
          self.meditation()
 
  def meditation(self):
    global meditation_active
    meditation_active = True
    print("The Jelly King's Champion uses Meditate.\nThe Jelly King's Champion has two times the defense!!!")

  
  def carnage(self, player, hero):
    damage = 100
    if player.ally == True and hero.is_dead == False:
      list_of_players = ['player', 'hero']
      if random.choice(list_of_players) == 'player':
        print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Carnage.{Style.RESET_ALL}")
        time.sleep(2)
        print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
        player.lose_health(damage)
      elif random.choice(list_of_players) == 'hero':
        print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Carnage.{Style.RESET_ALL}")
        time.sleep(2)
        print(f"{Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
        hero.lose_health(damage)
    elif player.ally == False or hero.is_dead == True:
        print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} uses {Fore.GREEN}Carnage.{Style.RESET_ALL}")
        time.sleep(2)
        print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
        player.lose_health(damage)

  def champ_attack(self, player, hero):
    if player_1.ally == True and hero.is_dead == False:
      player_attack = ['player', 'hero']
      if random.choice(player_attack) == 'player':  
        spell_chance = random.randint(1,4)
        if spell_chance == 1:
          print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}'{self.element}'.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}30 HP damage.{Style.RESET_ALL}")
          damage = 30
          player.lose_health(damage)
        else:
            if player_1.boots == True:
              if random.randint(1,4) == 1:
                damage = 0
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL} Your feet feel so light.")
              else:
                if player.ring == True:
                  prCyan("The Ring of Defense has Activated!")  
                  damage = round(random.randint(10,20) / 1.5)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                  elemental_damage = round(random.randint(5, 10) / 1.5) 
                  damage += elemental_damage
                  print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                  player.lose_health(damage)
                elif player.ring == False:
                  damage = random.randint(10,20)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                  elemental_damage = random.randint(5, 10) 
                  damage += elemental_damage
                  print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                  player.lose_health(damage)
            elif player_1.boots == False:  
              if random.randint(1,8) == 1:
                damage = 0
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL}")
              else:
                if player.ring == True:
                  prCyan("The Ring of Defense has Activated!")  
                  damage = round(random.randint(10,20) / 1.5)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                  elemental_damage = round(random.randint(5,10) / 1.5) 
                  damage += elemental_damage
                  print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                  player.lose_health(damage)
                elif player.ring == False:
                  damage = random.randint(10,20)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                  elemental_damage = random.randint(5,10) 
                  damage += elemental_damage
                  print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                  player.lose_health(damage)
                   
      elif random.choice(player_attack) == 'hero':
        spell_chance = random.randint(1,4)
        if spell_chance == 1:
          print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}'{self.element}'.{Style.RESET_ALL} {Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}30 HP damage.{Style.RESET_ALL}")
          damage = 30
          hero.lose_health(damage)
        else:
          if random.randint(1,6) == 1:
            damage = 0
            print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} misses {Fore.CYAN}{hero.name}!{Style.RESET_ALL}")
          else:
            damage = random.randint(20, 30)
            print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{hero.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
            hero.lose_health(damage)
    elif player_1.ally == False or hero_jelly.is_dead == True:
      spell_chance = random.randint(1,4)
      if spell_chance == 1:
        print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} casts {Fore.LIGHTGREEN_EX}'{self.element}'.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}30 HP damage.{Style.RESET_ALL}")
        damage = 30
        player.lose_health(damage)
      else:
          if player_1.boots == True:
            if random.randint(1,4) == 1:
              damage = 0
              print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL} Your feet feel so light.")
            else:
              if player.ring == True:
                prCyan("The Ring of Defense has Activated!")  
                damage = round(random.randint(10,20) / 1.5)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                elemental_damage = round(random.randint(5, 10) / 1.5) 
                damage += elemental_damage
                print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                player.lose_health(damage)
              elif player.ring == False:
                damage = random.randint(10,20)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                elemental_damage = random.randint(5, 10) 
                damage += elemental_damage
                print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                player.lose_health(damage)
          elif player_1.boots == False:  
            if random.randint(1,8) == 1:
              damage = 0
              print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} misses {Fore.CYAN}{player.name}!{Style.RESET_ALL}")
            else:
              if player.ring == True:
                prCyan("The Ring of Defense has Activated!")  
                damage = round(random.randint(10,20) / 1.5)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                elemental_damage = round(random.randint(5,10) / 1.5) 
                damage += elemental_damage
                print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                player.lose_health(damage)
              elif player.ring == False:
                damage = random.randint(10,20)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} attacks! {Fore.CYAN}{player.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                elemental_damage = random.randint(5,10) 
                damage += elemental_damage
                print(f"{Fore.CYAN}{player.name}{Style.RESET_ALL} suffers an additional {Fore.LIGHTRED_EX}{elemental_damage} HP{Style.RESET_ALL} of {Fore.LIGHTRED_EX}{self.element} damage.{Style.RESET_ALL}")
                player.lose_health(damage)
            
  def lose_health_champ(self, amount):
    if meditation_active == True:
      self.health -= round(amount / 2)
    elif meditation_active == False:
      self.health -= amount
    if self.health <= 0:
        self.champion_defeat()
    else:
        print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} has {Fore.YELLOW}{self.health} HP{Style.RESET_ALL} remaining.")
  
  def champion_defeat(self):
    print(f"The {Fore.GREEN}Jelly King's Champion{Style.RESET_ALL} has been defeated.")
    time.sleep(3)
    victory_list = range(0,10)
    for item in victory_list:
      prGreen("""
             Y   Y  OOO  U   U    W   W IIIII N   N  !
              Y Y  O   O U   U    W   W   I   NN  N  !
               Y   O   O U   U    W W W   I   N N N  !
               Y   O   O U   U    WW WW   I   N  NN  !
               Y    OOO   UUU     W   W IIIII N   N  .
               """)

    time.sleep(4) 
    os.system('clear||cls')
    if hero_jelly.is_dead == False and player_1.ally == True:
      print("You decide you've worn out your welcome here in Jelly Forest.\nOnce again history repeats itself as you look back at The Great Hero Jelly.\nIt nods back at you and smiles,\nkinda like that Robert Redford meme that everyone thinks is Zach Galifianakis.\nYou nod back at the Jelly, and decide it's time to be on your way.\nOn the beach you see a boat, ready to sail wherever the wind will take you.\nWhat adventures lie ahead? One thing is for certain, you'll never forget the time you had to...\nESCAPE FROM JELLY ISLAND!!!")
      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.")
      os.system('clear||cls')
      prCyan("""CREDITS:

      Development team: Austin Harry, Nolan Harry
      Lead Programmer: Austin Harry
      Creative Consultants: Joe Godwin, Erin Harry, Bill Bryan, Micah Harry

      THANK YOU FOR PLAYING!

      Find all of the endings!

      STAY TUNED FOR THE NEXT CHAPTER: JELLYBATTLE IN 2-D!!!
      Coming soon...

      """)

      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to exit.")
      quit()
    
    elif hero_jelly.is_dead == True:
      print("A sigh of relief comes out as you narrowly escape death once again.\nIt is a shame The Great Hero Jelly had to die, but his sacrifice will always be remembered.\nYou decide it's time to part ways with this place.\nAs the rain continues to pour down, you see a boat in the distance by the shore.\nUncertainty lies ahead as you decide to brave the trepid waters to escape.\nOne thing is for certain, you'll never forget the time you had to\nESCAPE FROM JELLY ISLAND!!!")
      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.")
      os.system('clear||cls')
      prCyan("""CREDITS:

      Development team: Austin Harry, Nolan Harry
      Lead Programmer: Austin Harry
      Creative Consultants: Joe Godwin, Erin Harry, Bill Bryan, Micah Harry

      THANK YOU FOR PLAYING!

      Find all of the endings!

      STAY TUNED FOR THE NEXT CHAPTER: JELLYBATTLE IN 2-D!!!
      Coming soon...
      
      """)

      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to exit.")
      quit()
    elif player_1.ally == False:
      print("A sense of relief falls over you as you narrowly escape death once again.\nEven though your adventure is over, you get the feeling that you missed something along the way.\nSorta like the feeling you get when you think you're forgetting something.\nOh well. You see a beach ahead of you with a boat by the shore. You decide to brave the waters to escape.\nOne thing is for certain, you'll never forget the time you had to\nESCAPE FROM JELLY ISLAND!!!")
      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.")
      os.system('clear||cls')
      prCyan("""CREDITS:

      Development team: Austin Harry, Nolan Harry
      Lead Programmer: Austin Harry
      Creative Consultants: Joe Godwin, Erin Harry, Bill Bryan, Micah Harry

      THANK YOU FOR PLAYING!

      Find all of the endings!

      STAY TUNED FOR THE NEXT CHAPTER: JELLYBATTLE IN 2-D!!!
      Coming soon...
      
      """)
      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to exit.")
      quit()
      


  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.ancient_defeat()
    else:
      print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} has {Fore.YELLOW}{self.health} HP{Style.RESET_ALL} remaining.")

  def ancient_defeat(self):
    global hero_jelly
    global player_1
    print(f"The {Fore.GREEN}Ancient Jelly{Style.RESET_ALL} has been defeated.")
    time.sleep(3)
    victory_list = range(0,10)
    for item in victory_list:
      prGreen("""
             Y   Y  OOO  U   U    W   W IIIII N   N  !
              Y Y  O   O U   U    W   W   I   NN  N  !
               Y   O   O U   U    W W W   I   N N N  !
               Y   O   O U   U    WW WW   I   N  NN  !
               Y    OOO   UUU     W   W IIIII N   N  .
               """)

    time.sleep(4) 
    
    player_1.gain_xp(30) 
    os.system('clear||cls')
    if hero_jelly.is_dead == False and player_1.ally == True:
      print("You decide you've worn out your welcome here at Jelly Castle.\nYou look back at The Great Hero Jelly, and it nods back at you and smiles,\nkinda like that Robert Redford meme that everyone thinks is Zach Galifianakis.\nYou nod back at the Jelly, and decide it's time to be on your way.\nYou head towards the forest entrance...")
      input("Press 'Enter' to continue.")
      hero_jelly.health = 100
      hero_jelly.potions = 3
      forest_entrance_room()
      
    elif hero_jelly.is_dead == True:
      print("A sigh of relief comes out as you narrowly escape death.\nIt is a shame The Great Hero Jelly had to die, but his sacrifice will always be remembered.\nYou decide it's time to part ways with this place.\nAs it starts to rain, you see a storm in the distance. Maybe it's a sign, or bad omen.\nA great forest lies before you. You decide to head in...")
      input("Press 'Enter' to continue.")
      forest_entrance_room()
    elif player_1.ally == False:
      print("A sense of relief falls over you as you narrowly escape death.\nNow that you've escaped the castle, you get the feeling that you missed something along the way.\nOh well. You see a great forest ahead of you. You decide to head in...")
      input("Press 'Enter' to continue.")
      forest_entrance_room()

    
# Setting up room functions for movement and game progression
def dungeon_cave_potion_in_room():
    global dungeon_cave_potion
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the flask? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the flask? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if potion_choice == 'yes':
        player_1.potions += 1 
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        dungeon_cave_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def dungeon_cave():
  global player_xp
  global jelly_1
  jelly_1.select_fake_element()
  global dungeon_cave_counter
  global dungeon_cave_potion
  if dungeon_cave_counter and player_1.note == True and player_1.monocle == True:
    print("You are back in what you assume to be the castle dungeon cave.\nBest not to dilly dally about.")
    if dungeon_cave_potion == True:
        print("You see the flask on the ground from earlier.")
        dungeon_cave_potion_in_room()
        os.system('clear||cls')
        print("You decide it's time to leave. You climb the ladder and return to the armory.")
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...")
        armory()
    elif dungeon_cave_potion == False:
        print("You decide it's time to leave. You climb the ladder and return to the armory.")
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...") 
        armory()
  elif dungeon_cave_counter > 0 and player_1.note == True:
    os.system('clear||cls')
    note_list = ['yes', 'no']
    print("You are back in what you assume to be the castle dungeon cave.\nBest not to dilly dally...wait. You see something reflect the light from the pile of burning books.\nIt appears to be a monocle. Will you use the monocle on the Note of Scribbles?")
    note_choice = input(f"Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while note_choice not in note_list:
        note_choice = input(f"Sorry, that is not a valid option.\nWill you use the monocle? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if note_choice == 'yes':
      print(f"You have received the {Fore.CYAN}Hero's Note!{Style.RESET_ALL}\nThe Note says to ring the bell at the forest entrance and the Hero will come to your aid!")
      player_1.monocle = True
      print("Well, it's time to go. Nothing else to see here. You climb back up the ladder leading to the armory.")
      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.") 
      armory()
    if note_choice == 'no':
      print("You have decided not to use the monocle. Guess we'll never know what that letter says. Sad day.")
      input(f"Time to head out, nothing else to see here. Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.")
      armory()
  elif dungeon_cave_counter > 0:
    os.system('clear||cls')
    print("You are back in what you assume to be the castle dungeon cave.\nBest not to dilly dally about.")
    if dungeon_cave_potion == True:
        print("You see the flask on the ground from earlier.")
        dungeon_cave_potion_in_room()
        os.system('clear||cls')
        print("You decide it's time to leave. You climb the ladder and return to the armory.")
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...")
        armory()
    elif dungeon_cave_potion == False:
        print("You decide it's time to leave. You climb the ladder and return to the armory.")
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...") 
        armory()
  elif dungeon_cave_counter == 0:
    os.system('clear||cls')
    print("You are surrounded in total darkness. You look at your arms, in shackles,\nwondering if you'll ever escape. Luckily, the wrist compass your father got you for your birthday is still intact.\nYou see a pile of books burning in the distance in a dark corner of the cave.\nYou hear something fall on the ground next to you.\nSomeone dropped a key from a small hole in the rock above!\nYou unlock your shackles and look around the dark, damp cave. You see a flask on the ground.")
    dungeon_cave_potion_in_room()
    print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
    print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
    time.sleep(1)
    battle_loop()
    os.system('clear||cls')
    print("You decide it's time to get moving, you see a ladder with a small hatch at the top.")
    print("You open the hatch and enter the next room.")
    input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...")
    dungeon_cave_counter += 1 
    time.sleep(2)
    armory()

def armory_sword_in_room():
    global armory_sword
    sword_list = ['yes', 'no']
    sword_choice = input(f"Will you pick up the sword? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while sword_choice not in sword_list:
        sword_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the sword? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if sword_choice == 'yes':
        player_1.sword = True  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has the {Fore.CYAN}Butterknife of Truth!{Style.RESET_ALL} Time to spread some {Fore.LIGHTGREEN_EX}Jelly.{Style.RESET_ALL}")
        time.sleep(2)
        armory_sword = False  
    elif sword_choice == 'no':
        player_1.sword = False
        print(f"{player_1.name} has left the sword for now.")
        time.sleep(2)

def armory():
    global jelly_1
    jelly_1.select_fake_element()
    jelly_1.reset_health()
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
            choice = input(f"Type {Fore.MAGENTA}'dungeon'{Style.RESET_ALL} to return to the Dungeon or type {Fore.MAGENTA}'door'{Style.RESET_ALL} to head through the ornate door.").lower()
            while choice != 'dungeon' and choice != 'door':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'dungeon'{Style.RESET_ALL} or {Fore.MAGENTA}'door'{Style.RESET_ALL}.").lower()
            if choice == 'dungeon':
                dungeon_cave()
            elif choice == 'door':
                dining_hall()
        elif armory_sword == False:
            print("You decide it's time to leave. Which way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'dungeon'{Style.RESET_ALL} to return to the Dungeon or type {Fore.MAGENTA}'door'{Style.RESET_ALL} to head through the ornate door.").lower()
            while choice != 'dungeon' and choice != 'door':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'dungeon'{Style.RESET_ALL} or {Fore.MAGENTA}'door'{Style.RESET_ALL}.").lower()
            if choice == 'dungeon':
                dungeon_cave()
            elif choice == 'door':
                dining_hall()
    elif armory_counter == 0:
        os.system('clear||cls')
        print("You take a look around a dimly lit room. You see various armaments such as\nswords and bows, and armor that looks too small for you to wear, probably designed with a Jelly in mind.\nOne sword in particular piques your interest.  As you approach the sword, you see the fine\ncraftsmanship and the ornate jewel encrusted hilt.  What a fine sword.")
        armory_sword_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Well, no time to waste. You see an ornate door leading from the armory.\nAlso behind you is the ladder leading back to the dungeon below.\nWhich way will you go?")
        armory_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'dungeon'{Style.RESET_ALL} to return to the Dungeon or type {Fore.MAGENTA}'door'{Style.RESET_ALL} to head through the ornate door.").lower()
        while choice != 'dungeon' and choice != 'door':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'dungeon'{Style.RESET_ALL} or {Fore.MAGENTA}'door'{Style.RESET_ALL}.").lower()
        if choice == 'dungeon':
            dungeon_cave()
        elif choice == 'door':
            dining_hall()
        time.sleep(2)

def dining_hall_potions_in_room():
    global dining_hall_potions
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    if potion_choice == 'yes':
        player_1.potions += 2  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        dining_hall_potions = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def dining_hall():
    global jelly_1
    jelly_1.select_fake_element()
    jelly_1.reset_health()
    global dining_hall_counter
    global dining_hall_potions
    list_of_choices = ['a', 'n', 's', 'g']
    if dining_hall_counter > 0:
        os.system('clear||cls')
        print("You are back in the spacious dining hall.\nIt seems no one has noticed the commotion going on.\nThe smell of fresh rolls makes your belly rumble.")
        if dining_hall_potions == True:
            print("You see the two potions on the table from earlier.")
            dining_hall_potions_in_room()
            os.system('clear||cls')
            print("You decide it's time to leave. You see the armory door, to the north is a set of double doors,\nto the south is a set of double doors with fresh roll smell coming from them,\nand to the west is a set of gold doors.\nWhich way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'a'{Style.RESET_ALL} to return to the armory, {Fore.MAGENTA}'n'{Style.RESET_ALL} for north doors,\n{Fore.MAGENTA}'s'{Style.RESET_ALL} for south doors or\n{Fore.MAGENTA}'g'{Style.RESET_ALL} for gold doors.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'a', 'n', 's',{Style.RESET_ALL} or {Fore.MAGENTA}'g'{Style.RESET_ALL}.").lower()
            if choice == 'a':
                armory()
            elif choice == 'n':
                foyer()
            elif choice == 's':
              kitchen()
            elif choice == 'g':
              throne_room()
        elif dining_hall_potions == False:
            print("You decide it's time to leave. You see the armory door, to the north is a set of double doors,\nto the south is a set of double doors with fresh roll smell coming from them,\nand to the west is a set of gold doors.\nWhich way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'a'{Style.RESET_ALL} to return to the armory, {Fore.MAGENTA}'n'{Style.RESET_ALL} for north doors,\n{Fore.MAGENTA}'s'{Style.RESET_ALL} for south doors or\n{Fore.MAGENTA}'g'{Style.RESET_ALL} for gold doors.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'a', 'n', 's',{Style.RESET_ALL} or {Fore.MAGENTA}'g'{Style.RESET_ALL}.").lower()
            if choice == 'a':
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
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Well, that was intense! Time to bounce. You see the armory door to the east.\nTo the north is a set of double doors, and to the south is a set of doors with faint fresh roll smell coming from them.\nTo the west is a large set of golden double doors. Which way will you go?")
        dining_hall_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'a'{Style.RESET_ALL} to return to the armory, {Fore.MAGENTA}'n'{Style.RESET_ALL} for north doors,\n{Fore.MAGENTA}'s'{Style.RESET_ALL} for south doors or\n{Fore.MAGENTA}'g'{Style.RESET_ALL} for gold doors.").lower()
        while choice not in list_of_choices:
            choice = input(f"Sorry, that's not a valid option. Type {Fore.MAGENTA}'a'{Style.RESET_ALL} to return to the armory, {Fore.MAGENTA}'n'{Style.RESET_ALL} for north doors,\n{Fore.MAGENTA}'s'{Style.RESET_ALL} for south doors or\n{Fore.MAGENTA}'g'{Style.RESET_ALL} for gold doors.").lower()
        if choice == 'a':
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
    sword_choice = input(f"Will you pick up the case knife? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while sword_choice not in sword_list:
        sword_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the case knife? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if sword_choice == 'yes':
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has the {Fore.CYAN}Case Knife of Deception!{Style.RESET_ALL}")
        time.sleep(2)
        prGreen("\nTHE KNIFE IS POISONED.")
        time.sleep(2)
        foyer_case_knife = False 
        player_1.death()
    elif sword_choice == 'no':
        foyer_case_knife = True
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} has left the case knife for now.")
        time.sleep(2)

def foyer():
    global jelly_1
    jelly_1.select_element("Fire")
    jelly_1.reset_health()
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
            choice = input(f"Type {Fore.MAGENTA}'d'{Style.RESET_ALL} to return to the dining hall, {Fore.MAGENTA}'e'{Style.RESET_ALL} for the doors with a visible stage through them to the east,\nor {Fore.MAGENTA}'exit'{Style.RESET_ALL} for the doors leading to the drawbridge.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'d', 'e',{Style.RESET_ALL} or {Fore.MAGENTA}'exit'.{Style.RESET_ALL}").lower()
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
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL} It's the last thing standing between you and freedom.")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("A sense of relief falls over you. Freedom is just a few yards away. The castle exit is before you.\nTo the east is a set of open double doors, with what appears to be a theater inside.\nBehind you is the dining hall. Where will you go?")
        foyer_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'d'{Style.RESET_ALL} to return to the dining hall, {Fore.MAGENTA}'e'{Style.RESET_ALL} for the doors with a visible stage through them to the east,\nor {Fore.MAGENTA}'exit'{Style.RESET_ALL} for the doors leading to the drawbridge.").lower()
        while choice not in list_of_choices:
            choice = input(f"Sorry, that is not a valid option.\nType {Fore.MAGENTA}'d'{Style.RESET_ALL} to return to the dining hall, {Fore.MAGENTA}'e'{Style.RESET_ALL} for the doors with a visible stage through them to the east,\nor {Fore.MAGENTA}'exit'{Style.RESET_ALL} for the doors leading to the drawbridge.").lower()
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
    potion_choice = input(f"Will you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if potion_choice == 'yes':
        player_1.potions += 1  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        kitchen_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)


def kitchen():
    global eat_cake
    global jelly_1
    jelly_1.chef_element()
    jelly_1.reset_health()
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
            choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to return north to the dining hall or type {Fore.MAGENTA}'w'{Style.RESET_ALL} to head west\nthrough the small door where you see many small beds, presumably the staff quarters.").lower()
            while choice != 'n' and choice != 'w':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n'{Style.RESET_ALL} or {Fore.MAGENTA}'w'.{Style.RESET_ALL}").lower()
            if choice == 'n':
                dining_hall()
            elif choice == 'w':
                staff_quarters()
        elif kitchen_potion == False:
            print("It smells so good in here. You're starving, but no time to waste. Which way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to return north to the dining hall or type {Fore.MAGENTA}'w'{Style.RESET_ALL} to head west\nthrough the small door where you see many small beds, presumably the staff quarters.").lower()
            while choice != 'n' and choice != 'w':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n'{Style.RESET_ALL} or {Fore.MAGENTA}'w'.{Style.RESET_ALL}").lower()
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
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        time.sleep(1)
        print("It has a chef's apron and hat.")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        chef_jelly_loop()
        os.system('clear||cls')
        print("Well, no time to eat after all. You see a small door to the west\nwhere you can see many small beds inside. Probably the staff quarters.\nTo the north are the doors leading back to the dining hall.\nWhich way will you go?")
        kitchen_counter += 1 
        eat_cake = False 
        choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to return north to the dining hall or type {Fore.MAGENTA}'w'{Style.RESET_ALL} to head west\nthrough the small door where you see many small beds, presumably the staff quarters.").lower()
        while choice != 'n' and choice != 'w':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n'{Style.RESET_ALL} or {Fore.MAGENTA}'w'{Style.RESET_ALL}.").lower()
        if choice == 'n':
            dining_hall()
        elif choice == 'w':
            staff_quarters()
        time.sleep(2)

def evasion_boots_in_room():
    global evasion_boots
    boots_list = ['yes', 'no']
    boots_choice = input(f"Will you pick up the boots? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    while boots_choice not in boots_list:
        boots_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the boots? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if boots_choice == 'yes':
        player_1.boots = True  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has the {Fore.CYAN}Evasion Boots!{Style.RESET_ALL} Their never gonna catch ya!")
        time.sleep(2)
        evasion_boots = False  
    elif boots_choice == 'no':
        player_1.boots = False
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} has left the boots for now.")
        time.sleep(2)

def throne_room():
    global jelly_1
    jelly_1.select_element("Ice")
    jelly_1.reset_health()
    global throne_room_counter
    global evasion_boots
    list_of_choices = ['d', 'r', 's']
    if throne_room_counter > 0:
        os.system('clear||cls')
        print("You are back in the throne room.\nStrange how no one is here, wonder what happened to the King and Queen?\nThose thrones sure look comfy...eh, nevermind, no time to waste!")
        if evasion_boots == True:
            print("You see the boots sitting next to the King's throne from earlier.")
            evasion_boots_in_room()
            os.system('clear||cls')
            print("It's time to move on. From where you came is the dining hall,\nto the north is what looks to be the royal quarters, judging by the elaborate golden door,\nand to the south is what looks to be the staff quarters, judging by the wooden door.")
            choice = input(f"Type {Fore.MAGENTA}'d'{Style.RESET_ALL} to return to the dining hall, {Fore.MAGENTA}'r'{Style.RESET_ALL} for the royal quarters,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} for the wooden door leading to the staff quarters.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'d', 'r',{Style.RESET_ALL} or {Fore.MAGENTA}'s'.{Style.RESET_ALL}").lower()
            if choice == 'd':
                dining_hall()
            elif choice == 'r':
                royal_quarters()
            elif choice == 's':
                staff_quarters()
        elif evasion_boots == False:
            print("It's time to move on. From where you came is the dining hall,\nto the north is what looks to be the royal quarters, judging by the elaborate golden door,\nand to the south is what looks to be the staff quarters, judging by the wooden door.")
            choice = input(f"Type {Fore.MAGENTA}'d'{Style.RESET_ALL} to return to the dining hall, {Fore.MAGENTA}'r'{Style.RESET_ALL} for the royal quarters,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} for the wooden door leading to the staff quarters.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'d', 'r',{Style.RESET_ALL} or {Fore.MAGENTA}'s'.{Style.RESET_ALL}").lower()
            if choice == 'd':
                dining_hall()
            elif choice == 'r':
                royal_quarters()
            elif choice == 's':
                staff_quarters()
    elif throne_room_counter == 0:
        os.system('clear||cls')
        print("You walk into a room with a huge chandelier hanging from the ceiling. You see two thrones side by side.\nThe throne on the left side is adorned with gold and jewels, the one on the right a bit smaller but still magnificent.\nYou see a huge carpet on the floor with a depiction of a Jelly war, and alongside the carpet\nare numerous small padded seats for what you assume to be royal guests.\nAn array of windows let the sunlight into the room and it reflects off the shiny checkered marble floor.\nYou see a pair of boots sitting beside the King's throne. How peculiar it is that boots made for a human reside in the castle.\nStrange indeed...")
        evasion_boots_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Now that the battle is over, you notice a large ornate golden door to the north, probably the royal quarters.\nTo the south you notice another door, much less extravagant, made of wood.\nBehind you is the door leading back to the dining hall. Where will you go?")
        throne_room_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'d'{Style.RESET_ALL} to return to the dining hall, {Fore.MAGENTA}'r'{Style.RESET_ALL} for the royal quarters door, or\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} for the doors leading to the staff quarters.").lower()
        while choice not in list_of_choices:
            choice = input(f"Sorry, that is not a valid option.\nType {Fore.MAGENTA}'d'{Style.RESET_ALL} to return to the dining hall, {Fore.MAGENTA}'r'{Style.RESET_ALL} for the royal quarters door,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} for the doors leading to the staff quarters.").lower()
        if choice == 'd':
          dining_hall()
        elif choice == 'r':
          royal_quarters()
        elif choice == 's':
          staff_quarters()
        time.sleep(2)

def staff_quarters_potion_in_room():
    global staff_quarters_potion
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potion? Please type{Fore.MAGENTA} 'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    if potion_choice == 'yes':
        player_1.potions += 1  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        staff_quarters_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def staff_quarters():
    global jelly_1
    jelly_1.sleepy_element()
    jelly_1.reset_health(60)
    global staff_quarters_counter
    global staff_quarters_potion 
    if staff_quarters_counter > 0:
        os.system('clear||cls')
        print("You are back in the staff quarters.\nAll of the commotion has died down for now.")
        if staff_quarters_potion == True:
            print("You see the potion on top of the bunk bed from earlier.")
            staff_quarters_potion_in_room()
            os.system('clear||cls')
            print("You sure could use a power nap. Oh well, no rest for the wicked. Which way are you headed?")
            choice = input(f"Type {Fore.MAGENTA}'k'{Style.RESET_ALL} to return to the kitchen or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north to the throne room.").lower()
            while choice != 'k' and choice != 'n':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'k'{Style.RESET_ALL} or {Fore.MAGENTA}'n'.{Style.RESET_ALL}").lower()
            if choice == 'k':
                kitchen()
            elif choice == 'n':
                print("Uh oh...It appears the door is locked. It must open from the other direction.")
                input(f"Please press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to return to the kitchen.")
                kitchen()
        elif staff_quarters_potion == False:
            print("You are back in the staff quarters.\nAll of the commotion has died down for now.")
            choice = input(f"Type {Fore.MAGENTA}'k'{Style.RESET_ALL} to return to the kitchen or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north to the throne room.").lower()
            while choice != 'k' and choice != 'n':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'k'{Style.RESET_ALL} or {Fore.MAGENTA}'n'.{Style.RESET_ALL}").lower()
            if choice == 'k':
                kitchen()
            elif choice == 'n':
                print("Uh oh...It appears the door is locked. It must open from the other direction.")
                input(f"Please press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to return to the kitchen.")
                kitchen()
    elif staff_quarters_counter == 0:
        os.system('clear||cls')
        print("You walk into a dimly lit room full of bunk beds and foot lockers.\nThere is a faint glow coming from the end of the room. Looks like flames from the fireplace.\nNot the most extravagant bedroom for the commoner, but not terribly bad either.\nThe beds are neatly made and they smell like fresh laundry. On top of one of the bunk beds, you see a potion.")
        kitchen_potion_in_room()
        print("You hear something rustling in one of the beds...")
        time.sleep(1)
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        time.sleep(1)
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}Tired {jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        sleepy_jelly_loop()
        os.system('clear||cls')
        print("Well, you probably spoiled that Jelly's nap. You see a small door to the north\nand to the east is the door to the kitchen. Sure smells good in there. Where are you headed?")
        staff_quarters_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'k'{Style.RESET_ALL} to head to the kitchen or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to use the north door.").lower()
        while choice != 'k' and choice != 'n':
            choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'k'{Style.RESET_ALL} or {Fore.MAGENTA}'n'{Style.RESET_ALL}.").lower()
        if choice == 'k':
                kitchen()
        elif choice == 'n':
            print("Uh oh...It appears the door is locked. It must open from the other direction.")
            input(f"Please press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to return to the kitchen.")
            kitchen()

def ring_in_royal_quarters():
    global defense_ring 
    ring_list = ['yes', 'no']
    ring_choice = input(f"Will you pick up the ring? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    while ring_choice not in ring_list:
        ring_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the ring? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    if ring_choice == 'yes':
        player_1.ring = True  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has the {Fore.CYAN}Ring of Defense!{Style.RESET_ALL} You know what they say--Defense wins championships!")
        time.sleep(2)
        defense_ring = False  
    elif ring_choice == 'no':
        player_1.ring = False
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} has left the ring for now.")
        time.sleep(2)

def royal_quarters():
  global jelly_1
  jelly_1.select_element("Wind")
  jelly_1.reset_health()
  global royal_quarters_counter
  global defense_ring
  if royal_quarters_counter > 0:
    os.system('clear||cls')
    print("You are back in the royal quarters.\nIt must be great to be royalty, regardless of if you are a Jelly or not.\n")
    if defense_ring == True:
        print("You see the ring on the nightstand from earlier.")
        ring_in_royal_quarters()
        os.system('clear||cls')
        print("Time to haul before someone sees you. You head back through the large gold ornate door to the throne room.")
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...")
        throne_room()
    elif defense_ring == False:
        print("Time to haul before someone sees you. You head back through the large gold ornate door to the throne room.")
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...") 
        throne_room()
  elif royal_quarters_counter == 0:
    os.system('clear||cls')
    print("You enter a large room with a gold ceiling. A giant bed sits before you,\nmade with hand-woven blankets and fur covered pillows.\nLarge tapestries hang down from the walls and a giant fur rug sits atop the shiny marble floor.\nYou see a small nightstand with a lamp sitting next to the bed.\nOn the nightstand you see a rather plain looking ring.")
    ring_in_royal_quarters()
    print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}") 
    print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
    time.sleep(1)
    battle_loop()
    os.system('clear||cls')
    print("Well, no more to do here for now. You head back through the large gold door to the throne room.")
    input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...")
    royal_quarters_counter += 1 
    time.sleep(2)
    throne_room()

def note_in_theater():
    global theater_note 
    note_list = ['yes', 'no']
    note_choice = input(f"Will you pick up the note? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    while note_choice not in note_list:
        note_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the note? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    if note_choice == 'yes':
        player_1.note = True  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has the {Fore.CYAN}Note of Scribbles!{Style.RESET_ALL} Too bad you can't understand the writing on the note.\nYou look on the back of the note and in your language you see the words: \"Perhaps you had better start from the beginning.\" Weird.")
        time.sleep(2)
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.")
        theater_note = False  
    elif note_choice == 'no':
        player_1.note = False
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} has left the note for now.")
        time.sleep(2)

def theater():
  global jelly_1
  jelly_1.select_element("Earth")
  jelly_1.reset_health()
  global theater_counter
  global theater_note
  if theater_counter > 0:
    os.system('clear||cls')
    print("You are back in the theater.\nThese Jelly shows must be grand productions. Would be neat to see one.")
    if theater_note == True:
        print("You see the note on the stage from earlier.")
        note_in_theater()
        os.system('clear||cls')
        print("Doesn't look like you'll be able to make the next showing. Gotta go. You head back through the door leading to the castle foyer.")
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...")
        foyer()
    elif theater_note == False:
        print("Doesn't look like you'll be able to make the next showing. Gotta go. You head back through the door leading to the castle foyer.")
        input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...") 
        foyer()
  elif theater_counter == 0:
    os.system('clear||cls')
    print("You enter a large hall with seats lined up on each side of the room.\nTwo sets of stairs wind up on each side of the room leading to a spacious balcony.\nAt the end of the hall is a large stage with red and gold colored curtains.\nIn front of the stage are steps leading down to an area with a music stand and some seating, probably for a Jelly chamber orchestra.\nAs you approach the stage, you see a worn piece of paper lying on the stage with incoherent scribbles on it.")
    note_in_theater()
    print(F"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}") 
    print(f"It appears to be a {Fore.LIGHTGREEN_EX}theatrical {jelly_1.element} Jelly.{Style.RESET_ALL}")
    time.sleep(1)
    battle_loop()
    os.system('clear||cls')
    print("Well, that was very entertaining. Time to make like a tree and get out of here.\nYou head back through the double doors to the castle foyer.")
    input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue...")
    theater_counter += 1 
    time.sleep(2)
    foyer()
  
def drawbridge():
   global drawbridge_counter
   if drawbridge_counter > 0:
      os.system('clear||cls')
      print("You're back outside the castle. as you head into the forest,\nYou remember the fantastic battle you fought here.\nWe can't rest on our laurels, time to move on.")
      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.")
      forest_entrance_room()
   elif drawbridge_counter == 0:   
      os.system('clear||cls') 
      print("You've finally made it out of the castle!\nYou smell the fresh air and feel the cool breeze on your face.\nYou begin to walk faster across the bridge over the clear water, and eventually\nbreak into a sprint. You make it across the bridge and see the front gates leading into a forest.\nAs you begin to enter the forest you here a voice that pierces your soul, almost like it's speaking to your mind.")
      time.sleep(3) 
      print("\nNOT SO FAST PRISONER! NOW YOU WILL PAY!") 
      input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.")
      drawbridge_counter += 1
      forest() 
  
def forest():
    if player_1.monocle == True:
      bell_choices = ['yes', 'no']
      choice = input(f"You see a wooden post with a large iron bell hanging from it. Will you ring the bell?\nPlease type {Fore.MAGENTA}'yes' or {Fore.MAGENTA}'no'.").lower()
      while choice not in bell_choices:
        choice = input(f"Sorry, that's not an option. Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}")
      if choice == 'yes':
          print(f"You ring the bell with all your might.\n{Fore.CYAN}THE GREAT HERO JELLY{Style.RESET_ALL} HAS APPEARED!\nIt's a little shorter than you thought.")
          player_1.ally = True
          print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} has appeared!!!")
          boss_loop_hero()
      if choice == 'no':
          print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} has appeared!!!")
          boss_loop_no_hero()
    if player_1.monocle == False:
      print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} has appeared!!!")
      boss_loop_no_hero()

def forest_entrance_potions_in_room():
    global forest_entrance_potions
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    if potion_choice == 'yes':
        player_1.potions += 2  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        forest_entrance_potions = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def forest_entrance_room():
    global jelly_1
    jelly_1.select_element("Thunder")
    jelly_1.reset_health(60)
    jelly_1.spell_enable()
    global forest_entrance_counter
    global forest_entrance_potions
    list_of_choices = ['n', 'e', 's', 'w']
    if forest_entrance_counter > 0:
        os.system('clear||cls')
        print("You are back at the forest entrance.\nYou can see the magnificent castle behind you,\nahead is a dirt path that splits into many directions\nleading further into the green sea of great pines before you.")
        if forest_entrance_potions == True:
            print("You see the two potions sitting next to the large tree\nin the center of the clearing from earlier.")
            forest_entrance_potions_in_room()
            os.system('clear||cls')
            print("Let's get going. From where you came is the magnificent castle,\nto the north is a path further into the forest,\nto the east is a path where you can see a small hut far in the distance,\n and to the west is another unremarkable path further into the forest.")
            choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north further in, {Fore.MAGENTA}'e'{Style.RESET_ALL} to head down the path towards the small hut in the distance,\n {Fore.MAGENTA}'s'{Style.RESET_ALL}to head back into the castle,\nand {Fore.MAGENTA}'w'{Style.RESET_ALL} to head down the unremarkable path further in.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n', 'e', 's',{Style.RESET_ALL} or {Fore.MAGENTA}'w'.{Style.RESET_ALL}").lower()
            if choice == 'n':
              forest_center()
            elif choice == 'e':
              path_to_hut()
            elif choice == 's':
              foyer()
            elif choice == 'w':
              forest_pond()
        elif forest_entrance_potions == False:
            print("Let's get going. From where you came is the magnificent castle,\nto the north is a path further into the forest,\nto the east is a path where you can see a small hut far in the distance,\n and to the west is another unremarkable path further into the forest.")
            choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north further in, {Fore.MAGENTA}'e'{Style.RESET_ALL} to head down the path towards the small hut in the distance,\n {Fore.MAGENTA}'s'{Style.RESET_ALL}to head back into the castle,\nand {Fore.MAGENTA}'w'{Style.RESET_ALL} to head down the unremarkable path further in.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n', 'e', 's',{Style.RESET_ALL} or {Fore.MAGENTA}'w'.{Style.RESET_ALL}").lower()
            if choice == 'n':
                forest_center()
            elif choice == 'e':
                path_to_hut()
            elif choice == 's':
                foyer()
            elif choice == 'w':
                forest_pond()
    elif forest_entrance_counter == 0:
        os.system('clear||cls')
        print("You breathe a sigh of relief. you see a great forest before you, and decide to enter.\nGreat Pine trees line a small dirt path that leads to a\nsmall clearing with a great pine tree in the center.\nYou see two potions lying beside the great tree.")
        forest_entrance_potions_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Now that we've handled that, you notice a few paths divulging into the woods.\nTo the north leads further into the woods, as well as another path to the west.\nBehind you and to the south is the magnificent castle.\nTo the east is a small narrow path, where you can barely make out what appears to be\na small hut. Which way shall you go?")
        forest_entrance_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to take the path north, {Fore.MAGENTA}'e'{Style.RESET_ALL} to take the narrow path towards the hut,\n{Fore.MAGENTA}'s'{Style.RESET_ALL} to head back into the castle, or {Fore.MAGENTA}'w'{Style.RESET_ALL} to take the west path further in.").lower()
        while choice not in list_of_choices:
            choice = input(f"Sorry, that is not a valid option.\nType {Fore.MAGENTA}'n', 'e', 's',{Style.RESET_ALL} or {Fore.MAGENTA}'w'.{Style.RESET_ALL}").lower()
        if choice == 'n':
          forest_center()
        elif choice == 'e':
          path_to_hut()
        elif choice == 's':
          foyer()
        elif choice == 'w':
          forest_pond()
        time.sleep(2)

def path_to_hut_potion_in_room():
    global path_to_hut_potion 
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if potion_choice == 'yes':
        player_1.potions += 1  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        path_to_hut_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def path_to_hut():
    global path_to_hut_potion
    global jelly_1
    jelly_1.select_element("Earth")
    jelly_1.reset_health(60)
    jelly_1.spell_enable()
    global path_to_hut_counter
    global path_to_hut_potion 
    if path_to_hut_counter > 0:
        os.system('clear||cls')
        print("You are back at the narrow path covered in brush. Looks like the commotion has died down.")
        if path_to_hut_potion == True:
            print("You see the potion in the brush from earlier.")
            path_to_hut_potion_in_room()
            os.system('clear||cls')
            print("You look at your arm, these scratches are starting to itch, hopefully you're not allergic.\nUnfortunately we have no time to waste. Which way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'w'{Style.RESET_ALL} to return to the forest entrance or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north\ntowards the small hut in the distance.").lower()
            while choice != 'w' and choice != 'n':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'w'{Style.RESET_ALL} or {Fore.MAGENTA}'n'.{Style.RESET_ALL}").lower()
            if choice == 'w':
                forest_entrance_room()
            elif choice == 'n':
                forest_hut()
        elif path_to_hut_potion == False:
            print("To the west lies the forest entrance,\nto the north you see a hut in the distance. Which way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'w'{Style.RESET_ALL} to return to the forest entrance or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north\ntowards the small hut in the distance.").lower()
            while choice != 'w' and choice != 'n':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'w'{Style.RESET_ALL} or {Fore.MAGENTA}'n'.{Style.RESET_ALL}").lower()
            if choice == 'w':
                forest_entrance_room()
            elif choice == 'n':
                forest_hut()
    elif path_to_hut_counter == 0:
        os.system('clear||cls')
        print("You see a small narrow path through a heavily wooded area.\nAs you make your way through the woods the path becomes obscured by heavy brush.\nYou squeeze through to keep on the path, the branches scratch your arms a little.\nYou see a potion stuck in the brush, someone probably dropped it and\ndidn't want to pick it up. Finders keepers, loosers weepers.")
        path_to_hut_potion_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        time.sleep(1)
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Wow, that was a tough battle considering how cramped up our fighting space was. Masterfully done.\nBack west is the entrance to the forest, north is the path heading to the hut.\nWhich way?")
        path_to_hut_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'w'{Style.RESET_ALL} to return west to the forest entrance or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north\nthrough the brush further down the path to the hut in the distance.").lower()
        while choice != 'w' and choice != 'n':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'w'{Style.RESET_ALL} or {Fore.MAGENTA}'n'{Style.RESET_ALL}.").lower()
        if choice == 'w':
            forest_entrance_room()
        elif choice == 'n':
            forest_hut()
        time.sleep(2)

def west_edge_potion_in_room():
    global west_edge_potion
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    if potion_choice == 'yes':
        player_1.potions += 1 
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        west_edge_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def west_edge():
    global jelly_1
    jelly_1.select_element("Fire")
    jelly_1.reset_health(60)
    jelly_1.spell_enable
    global west_edge_counter
    global west_edge_potion
    list_of_choices = ['n', 'e', 's']
    if west_edge_counter > 0:
        os.system('clear||cls')
        print("You are back at the large clearing with the fallen great pine.\nWonder if something hollowed out the giant trunk on purpose?")
        if west_edge_potion == True:
            print("You see the potion sitting in the log from earlier.")
            west_edge_potion_in_room()
            os.system('clear||cls')
            print("It's time to get a move on. To the north leads further in,\nto the east leads to a large clearing with the stream running beside it, and\n to the south you can see a pond.\nWhich way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head further in, {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the clearing with a stream,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} to head towards the pond.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n', 'e',{Style.RESET_ALL} or {Fore.MAGENTA}'s'{Style.RESET_ALL}.").lower()
            if choice == 'n':
                northwest_corner()
            elif choice == 'e':
                forest_center()
            elif choice == 's':
              forest_pond()
        elif west_edge_potion == False:
            print("It's time to get a move on. To the north leads further in,\nto the east leads to a large clearing with the stream running beside it, and\n to the south you can see a pond.\nWhich way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head further in, {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the clearing with a stream,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} to head towards the pond.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n', 'e',{Style.RESET_ALL} or {Fore.MAGENTA}'s'{Style.RESET_ALL}.").lower()
            if choice == 'n':
                northwest_corner()
            elif choice == 'e':
                forest_center()
            elif choice == 's':
              forest_pond()
    elif west_edge_counter == 0:
        os.system('clear||cls')
        print("As you head further into the forest you see a huge great pine that has fallen over.\nIt looks like the tree trunk has been hollowed out,\nmaybe to shelter some kind of animal or forest Jelly. I guess we'll never know.\nYou see a potion sitting inside the log.")
        west_edge_potion_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("It's time to get a move on. To the north leads further in,\nto the east leads to a large clearing with the stream running beside it, and\n to the south you can see a pond.\nWhich way will you go?")
        west_edge_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head further in, {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the clearing with a stream,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} to head towards the pond.").lower()
        while choice not in list_of_choices:
            choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n', 'e',{Style.RESET_ALL} or {Fore.MAGENTA}'s'{Style.RESET_ALL}.").lower()
        if choice == 'n':
          northwest_corner()
        elif choice == 'e':
          forest_center()
        elif choice == 's':
          forest_pond()
        time.sleep(2)

def northwest_corner_potion_in_room():
    global northwest_corner_potion 
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if potion_choice == 'yes':
        player_1.potions += 1  
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        northwest_corner_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def northwest_corner():
    global northwest_corner_potion
    global jelly_1
    jelly_1.select_element("Water")
    jelly_1.reset_health(60)
    jelly_1.spell_enable()
    global northwest_corner_counter
    global northwest_corner_potion 
    if northwest_corner_counter > 0:
        os.system('clear||cls')
        print("You are back at the northwest edge of the forest.\nYou think you can see the forest exit from here.")
        if northwest_corner_potion == True:
            print("You see the potion on the ground from earlier.")
            northwest_corner_potion_in_room()
            os.system('clear||cls')
            print("There is no time to lose, we gotta haul buns. Which way are we headed?")
            choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to head toward the forest exit or type {Fore.MAGENTA}'s'{Style.RESET_ALL} to head south\ntowards the great fallen pine in the distance.").lower()
            while choice != 'e' and choice != 's':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e'{Style.RESET_ALL} or {Fore.MAGENTA}'s'.{Style.RESET_ALL}").lower()
            if choice == 'e':
                forest_cave()
            elif choice == 's':
                west_edge()
        elif northwest_corner_potion == False:
            print("Almost out of the woods. Literally.\nBetter hurry while there's still daylight.")
            choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to head toward the forest exit or type {Fore.MAGENTA}'s'{Style.RESET_ALL} to head south\ntowards the great fallen pine in the distance.").lower()
            while choice != 'e' and choice != 's':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e'{Style.RESET_ALL} or {Fore.MAGENTA}'s'.{Style.RESET_ALL}").lower()
            if choice == 'e':
                forest_cave()
            elif choice == 's':
                west_edge()
    elif northwest_corner_counter == 0:
        os.system('clear||cls')
        print("As you continue it seems like you've been traveling for quite a while through this forest.\nYou see some light peeking through the trees up ahead.\nYou think you can see the exit of the forest up ahead and what appears to be a beach beyond.\nYou continue on forward. Wait... someone left a potion on the ground.")
        northwest_corner_potion_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        time.sleep(1)
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Glad that's over. To the south is a great fallen pine and to the east you can see the forest exit in the distance. Which way holmes?")
        northwest_corner_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to head toward the forest exit or type {Fore.MAGENTA}'s'{Style.RESET_ALL} to head south\ntowards the great fallen pine in the distance.").lower()
        while choice != 'e' and choice != 's':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e'{Style.RESET_ALL} or {Fore.MAGENTA}'s'{Style.RESET_ALL}.").lower()
        if choice == 'e':
            forest_cave()
        elif choice == 's':
            west_edge()
        time.sleep(2)

def forest_center_potions_in_room():
    global forest_center_potion
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potion? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    if potion_choice == 'yes':
        player_1.potions += 1 
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        forest_center_potion = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def forest_center():
    global jelly_1
    jelly_1.select_element("Ice")
    jelly_1.reset_health(60)
    jelly_1.spell_enable
    global forest_center_counter
    global forest_center_potion
    list_of_choices = ['n', 'e', 's', 'w']
    if forest_center_counter > 0:
        os.system('clear||cls')
        print("You are back at the forest center. You see the stream running along the clearing.")
        if forest_center_potion == True:
            print("You see the potion sitting by the stream bank from earlier.")
            forest_center_potions_in_room()
            os.system('clear||cls')
            print("You decide it's time to get moving. To the north leads further in, to the west is the clearing with a fallen pine,\n to the east is the hut, and to the south is the forest entrance.\nWhich way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head further in, {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the hut,\n{Fore.MAGENTA}'s'{Style.RESET_ALL} to head back to the forest entrance or\n{Fore.MAGENTA}'w'{Style.RESET_ALL} towards a clearing with a great fallen pine.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n', 'e', 's',{Style.RESET_ALL} or {Fore.MAGENTA}'w'{Style.RESET_ALL}.").lower()
            if choice == 'n':
                forest_cave()
            elif choice == 'e':
                forest_hut()
            elif choice == 's':
              forest_entrance_room()
            elif choice == 'w':
              west_edge()
        elif forest_center_potion == False:
            print("You decide it's time to get moving. To the north leads further in, to the west is the clearing with a fallen pine,\n to the east is the hut, and to the south is the forest entrance.\nWhich way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head further in, {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the hut,\n{Fore.MAGENTA}'s'{Style.RESET_ALL} to head back to the forest entrance or\n{Fore.MAGENTA}'w'{Style.RESET_ALL} towards a clearing with a great fallen pine.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n', 'e', 's',{Style.RESET_ALL} or {Fore.MAGENTA}'w'{Style.RESET_ALL}.").lower()
            if choice == 'n':
                forest_cave()
            elif choice == 'e':
                forest_hut()
            elif choice == 's':
              forest_entrance_room()
            elif choice == 'w':
              west_edge()
    elif forest_center_counter == 0:
        os.system('clear||cls')
        print("You come to a large clearing in the center of the woods, larger than the previous one.\nThere is a small stream that runs along the clearing.\nThe sound of the running water is very relaxing. You take a seat by the stream\nAnd notice someone left a potion by the stream bank.")
        forest_center_potions_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Well, that was something. No time to chill.\nTo the north leads further in, to the west is the clearing with a fallen pine,\n to the east is the hut, and to the south is the forest entrance.\nWhich way will you go?")
        forest_center_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head further in, {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the hut,\n{Fore.MAGENTA}'s'{Style.RESET_ALL} to head back to the forest entrance or\n{Fore.MAGENTA}'w'{Style.RESET_ALL} towards a clearing with a great fallen pine.").lower()
        while choice not in list_of_choices:
            choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'n', 'e', 's',{Style.RESET_ALL} or {Fore.MAGENTA}'w'{Style.RESET_ALL}.").lower()
        if choice == 'n':
          forest_cave()
        elif choice == 'e':
          forest_hut()
        elif choice == 's':
          forest_entrance_room()
        elif choice == 'w':
          west_edge()
        time.sleep(2)
  
def forest_pond_potions_in_room():
    global forest_pond_potions 
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if potion_choice == 'yes':
        player_1.potions += 2 
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        forest_pond_potions = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def forest_pond():
    global forest_pond_potions
    global jelly_1
    jelly_1.select_element("Wind")
    jelly_1.reset_health(60)
    jelly_1.spell_enable()
    global forest_pond_counter
    global forest_pond_potions 
    if forest_pond_counter > 0:
        os.system('clear||cls')
        print("As you look at the pond, you feel a sense of calmness wash over you.\nTo the east is the forest entrance,\nand to the north leads further in where you can see a great fallen pine.")
        if forest_pond_potions == True:
            print("You see the potions on the dock from earlier.")
            forest_pond_potions_in_room()
            os.system('clear||cls')
            print("You think to yourself maybe one day you can build a home by the pond.\nIt would be so relaxing. You could spend ev.....Snap out of it!\nWe gotta move. Which way will you go?")
            choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to return to the forest entrance or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north\nfurther into the forest.").lower()
            while choice != 'e' and choice != 'n':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e'{Style.RESET_ALL} or {Fore.MAGENTA}'n'.{Style.RESET_ALL}").lower()
            if choice == 'e':
                forest_entrance_room()
            elif choice == 'n':
                west_edge()
        elif forest_pond_potions == False:
            print("Been a while since you've been fishing, but there's no time.")
            choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to return to the forest entrance or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north\nfurther into the forest.").lower()
            while choice != 'e' and choice != 'n':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e'{Style.RESET_ALL} or {Fore.MAGENTA}'n'.{Style.RESET_ALL}").lower()
            if choice == 'e':
                forest_entrance_room()
            elif choice == 'n':
                west_edge()
    elif forest_pond_counter == 0:
        os.system('clear||cls')
        print("As you traverse the forest, you come to a large pond.\nThere is a small dock that has been built on the edge where there is a barrel full of fishing poles.\nDo Jellies eat fish? Who knows. Anyways, you see a couple of potions sitting on the dock.")
        forest_pond_potions_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        time.sleep(1)
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Now that the battle is over, you wonder if we have time for a swim.\nNot really, there's probably leeches in the water anyways...or pirahnas.\nHow do we proceed?")
        forest_pond_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to return east to the forest entrance or type {Fore.MAGENTA}'n'{Style.RESET_ALL} to head north\nfurther into the forest.").lower()
        while choice != 'e' and choice != 'n':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e'{Style.RESET_ALL} or {Fore.MAGENTA}'n'{Style.RESET_ALL}.").lower()
        if choice == 'e':
            forest_entrance_room()
        elif choice == 'n':
            west_edge()
        time.sleep(2)

def forest_hut_potions_in_room():
    global forest_hut_potions 
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    if potion_choice == 'yes':
        player_1.potions += 2 
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        forest_hut_potions = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def forest_hut():
    global forest_hut_potions
    global jelly_1
    jelly_1.select_element("Fart")
    jelly_1.reset_health(80)
    global forest_hut_counter
    global forest_hut_potions 
    if forest_hut_counter > 0:
        os.system('clear||cls')
        print("You are back at the forest hut.\nWonder if what the Fart Jelly said was true?\nProbably just crazy talk.")
        if forest_hut_potions == True:
            print("You see the potions on the ground from earlier.")
            forest_hut_potions_in_room()
            os.system('clear||cls')
            print("Well, we should probably get moving soon. To the south is the path to the hut\nand to the west is what appears to be a large clearing. Where we headed?")
            choice = input(f"Type {Fore.MAGENTA}'s'{Style.RESET_ALL} to return to the hut path or type {Fore.MAGENTA}'w'{Style.RESET_ALL} to head west\nfurther into the forest towards the large clearing.").lower()
            while choice != 's' and choice != 'w':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'s'{Style.RESET_ALL} or {Fore.MAGENTA}'w'.{Style.RESET_ALL}").lower()
            if choice == 's':
                path_to_hut()
            elif choice == 'w':
                forest_center()
        elif forest_hut_potions == False:
            print("You are back at the forest hut.\nWonder if what the Fart Jelly said was true?\nProbably just crazy talk.")
            choice = input(f"Type {Fore.MAGENTA}'s'{Style.RESET_ALL} to return to the forest entrance or type {Fore.MAGENTA}'w'{Style.RESET_ALL} to head west\nfurther into the forest.").lower()
            while choice != 's' and choice != 'w':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'s'{Style.RESET_ALL} or {Fore.MAGENTA}'w'.{Style.RESET_ALL}").lower()
            if choice == 's':
                path_to_hut()
            elif choice == 'w':
                forest_center()
    elif forest_hut_counter == 0:
        os.system('clear||cls')
        print("As you emerge through the brush, you arrive upon a small clearing\nwhere there is a hut crudely built from sticks and brush. As you approach you hear something rustling behind you.\nAs you turn to look you smell a very foul stench. You see a brown jelly before you. You notice a couple of potions on the ground, might want to hurry and pick those up!")
        forest_hut_potions_in_room()
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        time.sleep(1)
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        fart_jelly_loop()
        os.system('clear||cls')
        print(f"As the Fart Jelly fades away, He speaks to your mind.\nThings are not as they seem, your friends will betray you!\nThere is more to this than it appears!\nSounds like the Fart Jelly is a little off his rocker to me.\nThe {Fore.LIGHTGREEN_EX}Fart Jelly{Style.RESET_ALL} drops the {Fore.LIGHTGREEN_EX}Booty Bomb.{Style.RESET_ALL} You have picked up the {Fore.LIGHTGREEN_EX}Booty Bomb.{Style.RESET_ALL}")
        player_1.booty_bomb = True
        input("Press 'Enter' to continue.")
        os.system('clear||cls')
        print("Now that the battle is over, you wonder if what the Fart Jelly said is true?\nProbably just crazy talk. Where are we headed?")
        forest_hut_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'s'{Style.RESET_ALL} to return to the hut path or type {Fore.MAGENTA}'w'{Style.RESET_ALL} to head west\nfurther into the forest, towards the clearing.").lower()
        while choice != 's' and choice != 'w':
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'s'{Style.RESET_ALL} or {Fore.MAGENTA}'w'{Style.RESET_ALL}.").lower()
        if choice == 's':
            path_to_hut()
        elif choice == 'w':
            forest_center()
        time.sleep(2)

def forest_cave_potions_in_room():
    global forest_cave_potions
    potion_list = ['yes', 'no']
    potion_choice = input(f"Will you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'{Style.RESET_ALL}.").lower()
    while potion_choice not in potion_list:
        potion_choice = input(f"Sorry, that is not a valid option.\nWill you pick up the potions? Please type {Fore.MAGENTA}'yes'{Style.RESET_ALL} or {Fore.MAGENTA}'no'.{Style.RESET_ALL}").lower()
    if potion_choice == 'yes':
        player_1.potions += 2 
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)
        forest_cave_potions = False  
    elif potion_choice == 'no':
        player_1.potions += 0
        print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} now has {Fore.YELLOW}{player_1.potions} potions.{Style.RESET_ALL}")
        time.sleep(2)

def forest_cave():
    global jelly_1
    jelly_1.select_element("Ice")
    jelly_1.reset_health(60)
    jelly_1.spell_enable
    global forest_cave_counter
    global forest_cave_potions
    list_of_choices = ['e', 'w', 's']
    if forest_cave_counter > 0:
        os.system('clear||cls')
        print("You are back at the large clearing with the cave nestled in the rocks.\nShould we go explore it?...Eh, maybe not.")
        if forest_cave_potions == True:
            print("You see the potions sitting by the cave entrance from earlier.")
            forest_cave_potions_in_room()
            os.system('clear||cls')
            print("Time to roll out. To the east lies the forest exit,\nto the south is the large clearing with the stream,\n and to the west is the northwest corner of the forest.\nWhich way will we go?")
            choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the forest exit, {Fore.MAGENTA}'w'{Style.RESET_ALL} to head to the northwest corner of the forest,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} to head towards the clearing with the stream.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e', 'w',{Style.RESET_ALL} or {Fore.MAGENTA}'s'{Style.RESET_ALL}.").lower()
            if choice == 'w':
                northwest_corner()
            elif choice == 's':
                forest_center()
            elif choice == 'e':
              forest_exit()
        elif forest_cave_potions == False:
            print("Time to roll out. To the east lies the forest exit,\nto the south is the large clearing with the stream,\n and to the west is the northwest corner of the forest.\nWhich way will we go?")
            choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the forest exit, {Fore.MAGENTA}'w'{Style.RESET_ALL} to head to the northwest corner of the forest,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} to head towards the clearing with the stream.").lower()
            while choice not in list_of_choices:
              choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e', 'w',{Style.RESET_ALL} or {Fore.MAGENTA}'s'{Style.RESET_ALL}.").lower()
            if choice == 'w':
                northwest_corner()
            elif choice == 's':
                forest_center()
            elif choice == 'e':
              forest_exit()
    elif forest_cave_counter == 0:
        os.system('clear||cls')
        print("As you continue further on the light at the end of the forest gets a little bit brighter.\nTo the north you see a cave settled into the rocks.\n It's very dark and ominous looking. You feel like maybe we should skip the exploration for now.\nAt the entrance to the cave you see a couple of potions lying on the ground.")
        forest_cave_potions_in_room()
        print("Something is emerging from the darkness.")
        print(f"A {Fore.LIGHTGREEN_EX}JELLY APPROACHES!{Style.RESET_ALL}")
        print(f"It appears to be a {Fore.LIGHTGREEN_EX}{jelly_1.element} Jelly.{Style.RESET_ALL}")
        time.sleep(1)
        battle_loop()
        os.system('clear||cls')
        print("Time to roll out. To the east lies the forest exit,\nto the south is the large clearing with the stream,\n and to the west is the northwest corner of the forest.\nWhich way will we go?")
        forest_cave_counter += 1 
        choice = input(f"Type {Fore.MAGENTA}'e'{Style.RESET_ALL} to head towards the forest exit, {Fore.MAGENTA}'w'{Style.RESET_ALL} to head to the northwest corner of the forest,\nor {Fore.MAGENTA}'s'{Style.RESET_ALL} to head towards the clearing with the stream.").lower()
        while choice not in list_of_choices:
           choice = input(f"Sorry, that is not a valid option. Please type {Fore.MAGENTA}'e', 'w',{Style.RESET_ALL} or {Fore.MAGENTA}'s'{Style.RESET_ALL}.").lower() 
        if choice == 'w':
          northwest_corner()
        elif choice == 's':
          forest_center()
        elif choice == 'e':
          forest_exit()
        time.sleep(2)

def forest_exit():
  global champ_jelly
  champ_jelly.select_champ_element()
  os.system('clear||cls')
  print("You see the exit to the forest lying before you.\nThe light peeks through the trees and you see what appears to be a beach and a large body of water.\nAnother voice speaks to your mind. It says, \"Halt! You are under arrest for treason!\nYou are to be executed by the order of the King!\"\nA fearsome looking jelly on a horse rides up to you. He says, \"I am the king's champion. you will pay for your crimes!\"")
  input(f"Press {Fore.MAGENTA}'Enter'{Style.RESET_ALL} to continue.")
  os.system('clear||cls')
  print(f"THE {Fore.LIGHTGREEN_EX}JELLY KING'S CHAMPION APPROACHES!{Style.RESET_ALL}")
  time.sleep(1)
  if player_1.booty_bomb == True:
    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} uses the {Fore.LIGHTGREEN_EX}Booty Bomb!{Style.RESET_ALL} The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL}")
  
  if player_1.ally == True and hero_jelly.is_dead == False:
    print(f"The {Fore.CYAN}Great Hero Jelly Appears!{Style.RESET_ALL} He still seems a little short to you.")
    champion_loop_hero()
  elif player_1.ally == False or hero_jelly.is_dead == True:
    champion_loop_no_hero()
  





  


def battle_loop():
  player_1.flee_chance = False
  if player_1.axe==True:
    while player_1.health > 0 and jelly_1.health > 0:
        choice_list = ['attack', 'run', 'potion', 'axe', 'make friends']
        choice = input(f"Please type {Fore.MAGENTA}'attack', 'axe', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'{Style.RESET_ALL}.  ").lower()
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
        elif choice == "axe":
            time.sleep(0.5)
            player_1.elemental_attack(jelly_1)
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
  elif player_1.axe ==False:  
    while player_1.health > 0 and jelly_1.health > 0:
        choice_list = ['attack', 'run', 'potion', 'make friends']
        choice = input(f"Please type {Fore.MAGENTA}'attack', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'{Style.RESET_ALL}.  ").lower()
        player_1.flee_chance = False
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

cake_counter = 0
def chef_jelly_loop():
  player_1.flee_chance = False
  global cake_counter
  while player_1.health > 0 and jelly_1.health > 0 and eat_cake == False:
    if cake_counter >= 3:
      jelly_1.bake_cake(player_1)
    else:
      if player_1.axe == True:
          choice_list = ['attack', 'axe', 'run', 'potion', 'make friends']
          choice = input(f"Please type {Fore.MAGENTA}'attack', 'axe', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'{Style.RESET_ALL}.  ").lower()
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
                  jelly_1.chef_attack(player_1)
                  time.sleep(0.5)
                  cake_counter += 1
          elif choice == "axe":
              time.sleep(0.5)
              player_1.elemental_attack(jelly_1)
              time.sleep(1)
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.chef_attack(player_1)
                  time.sleep(0.5)
                  cake_counter += 1
          elif choice == "potion":
              time.sleep(0.5)
              player_1.use_potion()
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.chef_attack(player_1)
                  cake_counter += 1
                  time.sleep(0.5)
          elif choice == "run":
              time.sleep(0.5)
              player_1.flee()
              if player_1.flee_chance == True:
                  break
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.chef_attack(player_1)
                  cake_counter += 1
                  time.sleep(0.5)
      elif player_1.axe == False:
          choice_list = ['attack', 'run', 'potion', 'make friends']
          choice = input(f"Please type {Fore.MAGENTA}'attack', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'{Style.RESET_ALL}.  ").lower()
          player_1.flee_chance = False
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
                  jelly_1.chef_attack(player_1)
                  time.sleep(0.5)
                  cake_counter += 1
          elif choice == "potion":
              time.sleep(0.5)
              player_1.use_potion()
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.chef_attack(player_1)
                  cake_counter += 1
                  time.sleep(0.5)
          elif choice == "run":
              time.sleep(0.5)
              player_1.flee()
              if player_1.flee_chance == True:
                  break
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.chef_attack(player_1)
                  cake_counter += 1
                  time.sleep(0.5)

spare_counter = 0
def sleepy_jelly_loop():
  player_1.flee_chance = False
  global spare_counter
  while player_1.health > 0 and jelly_1.health > 0 and player_1.axe==False:
    if spare_counter >= 3:
        player_1.spare_sleepy_jelly()
    else:    
        choice_list = ['attack', 'run', 'potion', 'make friends']
        choice = input(f"Please type {Fore.MAGENTA}'attack', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'{Style.RESET_ALL}.  ").lower()
        player_1.flee_chance = False
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
                jelly_1.sleepy_attack(player_1)
                time.sleep(0.5)
                spare_counter += 1
        elif choice == "potion":
            time.sleep(0.5)
            player_1.use_potion()
            if jelly_1.health > 0:
                time.sleep(0.5)
                jelly_1.sleepy_attack(player_1)
                spare_counter += 1
                time.sleep(0.5)
        elif choice == "run":
            time.sleep(0.5)
            player_1.flee()
            if player_1.flee_chance == True:
                break
            if jelly_1.health > 0:
                time.sleep(0.5)
                jelly_1.sleepy_attack(player_1)
                spare_counter += 1
                time.sleep(0.5)

sbd_counter = 0
def fart_jelly_loop():
  player_1.flee_chance = False
  global sbd_counter
  while player_1.health > 0 and jelly_1.health > 0:
    if sbd_counter >= 3 and player_1.is_poisoned == False:
      jelly_1.sbd_attack(player_1)
    else:
      if player_1.axe == True:
          choice_list = ['attack', 'axe', 'run', 'potion', 'make friends']
          choice = input(f"Please type {Fore.MAGENTA}'attack', 'axe', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'{Style.RESET_ALL}.  ").lower()
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
                  jelly_1.fart_attack(player_1)
                  time.sleep(0.5)
                  sbd_counter += 1
                  if player_1.is_poisoned == True:
                    damage = random.randint(5,10)
                    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                    player_1.lose_health(damage)
                    sbd_counter -= 2
                    if sbd_counter <= 0:
                      print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is no longer {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL}")
                      player_1.is_poisoned = False
          elif choice == "axe":
              time.sleep(0.5)
              player_1.elemental_attack(jelly_1)
              time.sleep(1)
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.fart_attack(player_1)
                  time.sleep(0.5)
                  sbd_counter += 1
                  if player_1.is_poisoned == True:
                    damage = random.randint(5,10)
                    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                    player_1.lose_health(damage)
                    sbd_counter -= 2
                    if sbd_counter <= 0:
                      print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is no longer {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL}")
                      player_1.is_poisoned = False
          elif choice == "potion":
              time.sleep(0.5)
              player_1.use_potion()
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.fart_attack(player_1)
                  sbd_counter += 1
                  time.sleep(0.5)
                  if player_1.is_poisoned == True:
                    damage = random.randint(5,10)
                    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                    player_1.lose_health(damage)
                    sbd_counter -= 2
                    if sbd_counter <= 0:
                      print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is no longer {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL}")
                      player_1.is_poisoned = False
          elif choice == "run":
              time.sleep(0.5)
              print(f"The {Fore.LIGHTGREEN_EX}Fart Jelly{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}'Telekinesis'{Style.RESET_ALL}. You can't run!")
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.fart_attack(player_1)
                  sbd_counter += 1
                  time.sleep(0.5)
                  if player_1.is_poisoned == True:
                    damage = random.randint(5,10)
                    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                    player_1.lose_health(damage)
                    sbd_counter -= 2
                    if sbd_counter <= 0:
                      print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is no longer {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL}")
                      player_1.is_poisoned = False
      elif player_1.axe == False:
          choice_list = ['attack', 'run', 'potion', 'make friends']
          choice = input(f"Please type {Fore.MAGENTA}'attack', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'{Style.RESET_ALL}.  ").lower()
          player_1.flee_chance = False
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
                  jelly_1.fart_attack(player_1)
                  time.sleep(0.5)
                  sbd_counter += 1
                  if player_1.is_poisoned == True:
                    damage = random.randint(5,10)
                    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                    player_1.lose_health(damage)
                    sbd_counter -= 2
                    if sbd_counter <= 0:
                      print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is no longer {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL}")
                      player_1.is_poisoned = False
          elif choice == "potion":
              time.sleep(0.5)
              player_1.use_potion()
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.fart_attack(player_1)
                  sbd_counter += 1
                  time.sleep(0.5)
                  if player_1.is_poisoned == True:
                    damage = random.randint(5,10)
                    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                    player_1.lose_health(damage)
                    sbd_counter -= 2
                    if sbd_counter <= 0:
                      print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is no longer {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL}")
                      player_1.is_poisoned = False
          elif choice == "run":
              time.sleep(0.5)
              print(f"The {Fore.LIGHTGREEN_EX}Fart Jelly{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}'Telekinesis'{Style.RESET_ALL}. You can't run!")
              if jelly_1.health > 0:
                  time.sleep(0.5)
                  jelly_1.fart_attack(player_1)
                  sbd_counter += 1
                  time.sleep(0.5)
                  if player_1.is_poisoned == True:
                    damage = random.randint(5,10)
                    print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL} {Fore.CYAN}{player_1.name}{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{damage} HP damage.{Style.RESET_ALL}")
                    player_1.lose_health(damage)
                    sbd_counter -= 2
                    if sbd_counter <= 0:
                      print(f"{Fore.CYAN}{player_1.name}{Style.RESET_ALL} is no longer {Fore.LIGHTGREEN_EX}POISONED.{Style.RESET_ALL}")
                      player_1.is_poisoned = False

       
def boss_loop_no_hero():
  boss_counter = 0
  celestial_counter = 4
  while player_1.health > 0 and boss_jelly.health > 0:
    if celestial_counter == 0:
      boss_jelly.celestial_doom(player_1, hero_jelly)    
    else:
      if player_1.axe == True:
        choice_list = ['attack', 'axe', 'run', 'potion', 'make friends']
        choice = input(f"Please type {Fore.MAGENTA}'attack', 'axe', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'.{Style.RESET_ALL}  ").lower()
        player_1.flee_chance = False
        if choice not in choice_list:
            time.sleep(0.5)
            print("Ha Ha, you're funny. Sorry, that's not an available option."  )
        elif choice == "make friends":
            time.sleep(1)
            print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is not very friendly, unfortunately.")
            time.sleep(0.5)
            
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
             boss_jelly.millenium_reminisce(player_1, hero_jelly) 
             boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        elif choice == "attack":
            time.sleep(0.5)
            player_1.attack(boss_jelly)
            
            time.sleep(1)
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
              boss_jelly.millenium_reminisce(player_1, hero_jelly)
              boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        elif choice == 'axe':
            time.sleep(0.5)
            player_1.elemental_attack(boss_jelly)
            time.sleep(1)
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
              boss_jelly.millenium_reminisce(player_1, hero_jelly)
              boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        elif choice == "potion":
            time.sleep(0.5)
            player_1.use_potion()
            
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
             boss_jelly.millenium_reminisce(player_1, hero_jelly)
             boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        elif choice == "run":
            time.sleep(0.5)
            print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Telekinesis.{Style.RESET_ALL} You can't run!?!")
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
             boss_jelly.millenium_reminisce(player_1, hero_jelly)
             boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
      elif player_1.axe == False:  
        choice_list = ['attack', 'run', 'potion', 'make friends']
        choice = input(f"Please type {Fore.MAGENTA}'attack', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'.{Style.RESET_ALL}  ").lower()
        player_1.flee_chance = False
        if choice not in choice_list:
            time.sleep(0.5)
            print("Ha Ha, you're funny. Sorry, that's not an available option."  )
        elif choice == "make friends":
            time.sleep(1)
            print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is not very friendly, unfortunately.")
            time.sleep(0.5)
            
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
             boss_jelly.millenium_reminisce(player_1, hero_jelly) 
             boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        elif choice == "attack":
            time.sleep(0.5)
            player_1.attack(boss_jelly)
            
            time.sleep(1)
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
              boss_jelly.millenium_reminisce(player_1, hero_jelly)
              boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        elif choice == "potion":
            time.sleep(0.5)
            player_1.use_potion()
            
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
             boss_jelly.millenium_reminisce(player_1, hero_jelly)
             boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        elif choice == "run":
            time.sleep(0.5)
            print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Telekinesis.{Style.RESET_ALL} You can't run!?!")
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
             boss_jelly.millenium_reminisce(player_1, hero_jelly)
             boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                  boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        
def boss_loop_hero():
    boss_counter = 0
    celestial_counter = 4
    while player_1.health > 0 and boss_jelly.health > 0:
      if celestial_counter == 0:
        boss_jelly.celestial_doom(player_1, hero_jelly)    
      else:
        if player_1.axe == True:
          choice_list = ['attack', 'axe', 'run', 'potion', 'make friends']
          choice = input(f"Please type {Fore.MAGENTA}'attack', 'run', 'axe',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'.{Style.RESET_ALL}  ").lower()
          player_1.flee_chance = False
          if choice not in choice_list:
              time.sleep(0.5)
              print("Ha Ha, you're funny. Sorry, that's not an available option."  )
          elif choice == "make friends":
              time.sleep(1)
              print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is not very friendly, unfortunately.")
              time.sleep(0.5)
              hero_jelly.attack(boss_jelly, player_1)
              if boss_jelly.health >= 50 and boss_counter % 3 == 1:
                boss_jelly.millenium_reminisce(player_1, hero_jelly) 
                boss_counter += 1
              elif boss_jelly.health >= 50:
                  time.sleep(0.5)
                  boss_jelly.attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  boss_counter += 1
              elif boss_jelly.health < 50:
                  celestial_counter -= 1
                  if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                  print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
          elif choice == "attack":
              time.sleep(0.5)
              player_1.attack(boss_jelly)
              time.sleep(0.5)
              hero_jelly.attack(boss_jelly, player_1)
              time.sleep(1)
              if boss_jelly.health >= 50 and boss_counter % 3 == 1:
                boss_jelly.millenium_reminisce(player_1, hero_jelly)
                boss_counter += 1
              elif boss_jelly.health >= 50:
                  time.sleep(0.5)
                  boss_jelly.attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  boss_counter += 1
              elif boss_jelly.health < 50:
                  celestial_counter -= 1
                  if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                  print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
          elif choice == 'axe':
              time.sleep(0.5)
              player_1.elemental_attack(boss_jelly)
              time.sleep(0.5)
              hero_jelly.attack(boss_jelly, player_1)
              time.sleep(1)
              if boss_jelly.health >= 50 and boss_counter % 3 == 1:
                boss_jelly.millenium_reminisce(player_1, hero_jelly)
                boss_counter += 1
              elif boss_jelly.health >= 50:
                  time.sleep(0.5)
                  boss_jelly.attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  boss_counter += 1
              elif boss_jelly.health < 50:
                  celestial_counter -= 1
                  if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                  print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
          elif choice == "potion":
            heal_list = ['p', 'h']
            heal_choice = input(f"Who will recieve the potion? Please type {Fore.MAGENTA}'p'{Style.RESET_ALL} for {Fore.CYAN}Player{Style.RESET_ALL} or {Fore.MAGENTA}'h'{Style.RESET_ALL} for {Fore.CYAN}Hero Jelly.{Style.RESET_ALL}").lower() 
            while heal_choice not in heal_list:
              heal_choice = input(f"Sorry, that is not a valid option. Please press {Fore.MAGENTA}'p'{Style.RESET_ALL} for {Fore.CYAN}Player{Style.RESET_ALL} or {Fore.MAGENTA}'h'{Style.RESET_ALL} for {Fore.CYAN}Hero Jelly.{Style.RESET_ALL}").lower()
              time.sleep(0.5)
            if heal_choice == 'p':
              player_1.use_potion()
            elif heal_choice == 'h':
              player_1.use_potion_ally(hero_jelly)
            hero_jelly.attack(boss_jelly, player_1)
            time.sleep(0.5)
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
              boss_jelly.millenium_reminisce(player_1, hero_jelly)
              boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
          elif choice == "run":
              time.sleep(0.5)
              print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Telekinesis.{Style.RESET_ALL} You can't run!?!")
              hero_jelly.attack(boss_jelly, player_1)
              time.sleep(0.5)
              if boss_jelly.health >= 50 and boss_counter % 3 == 1:
                boss_jelly.millenium_reminisce(player_1, hero_jelly)
                boss_counter += 1
              elif boss_jelly.health >= 50:
                  time.sleep(0.5)
                  boss_jelly.attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  boss_counter += 1
              elif boss_jelly.health < 50:
                  celestial_counter -= 1
                  if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                  print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
        elif player_1.axe == False:  
          choice_list = ['attack', 'run', 'potion', 'make friends']
          choice = input(f"Please type {Fore.MAGENTA}'attack', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'.{Style.RESET_ALL}  ")
          player_1.flee_chance = False
          if choice not in choice_list:
              time.sleep(0.5)
              print("Ha Ha, you're funny. Sorry, that's not an available option."  )
          elif choice == "make friends":
              time.sleep(1)
              print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is not very friendly, unfortunately.")
              time.sleep(0.5)
              hero_jelly.attack(boss_jelly, player_1)
              if boss_jelly.health >= 50 and boss_counter % 3 == 1:
                boss_jelly.millenium_reminisce(player_1, hero_jelly) 
                boss_counter += 1
              elif boss_jelly.health >= 50:
                  time.sleep(0.5)
                  boss_jelly.attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  boss_counter += 1
              elif boss_jelly.health < 50:
                  celestial_counter -= 1
                  if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                  print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
          elif choice == "attack":
              time.sleep(0.5)
              player_1.attack(boss_jelly)
              time.sleep(0.5)
              hero_jelly.attack(boss_jelly, player_1)
              time.sleep(1)
              if boss_jelly.health >= 50 and boss_counter % 3 == 1:
                boss_jelly.millenium_reminisce(player_1, hero_jelly)
                boss_counter += 1
              elif boss_jelly.health >= 50:
                  time.sleep(0.5)
                  boss_jelly.attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  boss_counter += 1
              elif boss_jelly.health < 50:
                  celestial_counter -= 1
                  if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                  print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
          elif choice == "potion":
            heal_list = ['p', 'h']
            heal_choice = input(f"Who will recieve the potion? Please type {Fore.MAGENTA}'p'{Style.RESET_ALL} for {Fore.CYAN}Player{Style.RESET_ALL} or {Fore.MAGENTA}'h'{Style.RESET_ALL} for {Fore.CYAN}Hero Jelly.{Style.RESET_ALL}").lower() 
            while heal_choice not in heal_list:
              heal_choice = input(f"Sorry, that is not a valid option. Please press {Fore.MAGENTA}'p'{Style.RESET_ALL} for {Fore.CYAN}Player{Style.RESET_ALL} or {Fore.MAGENTA}'h'{Style.RESET_ALL} for {Fore.CYAN}Hero Jelly.{Style.RESET_ALL}").lower()
              time.sleep(0.5)
            if heal_choice == 'p':
              player_1.use_potion()
            elif heal_choice == 'h':
              player_1.use_potion_ally(hero_jelly)
            hero_jelly.attack(boss_jelly, player_1)
            time.sleep(0.5)
            if boss_jelly.health >= 50 and boss_counter % 3 == 1:
              boss_jelly.millenium_reminisce(player_1, hero_jelly)
              boss_counter += 1
            elif boss_jelly.health >= 50:
                time.sleep(0.5)
                boss_jelly.attack(player_1, hero_jelly)
                time.sleep(0.5)
                boss_counter += 1
            elif boss_jelly.health < 50:
                celestial_counter -= 1
                if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")
          elif choice == "run":
              time.sleep(0.5)
              print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Telekinesis.{Style.RESET_ALL} You can't run!?!")
              hero_jelly.attack(boss_jelly, player_1)
              time.sleep(0.5)
              if boss_jelly.health >= 50 and boss_counter % 3 == 1:
                boss_jelly.millenium_reminisce(player_1, hero_jelly)
                boss_counter += 1
              elif boss_jelly.health >= 50:
                  time.sleep(0.5)
                  boss_jelly.attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  boss_counter += 1
              elif boss_jelly.health < 50:
                  celestial_counter -= 1
                  if boss_jelly.potions != 0:
                    boss_jelly.use_ancient_potion()
                  print(f"The {Fore.LIGHTGREEN_EX}Ancient Jelly{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Celestial Doom...{Style.RESET_ALL}in {celestial_counter}...")

def champion_loop_hero():
  global champ_boss_counter 
  global carnage_counter 
  while player_1.health > 0 and champ_jelly.health > 0:
    if hero_jelly.is_dead == False:
    
      if carnage_counter == 0:
        champ_jelly.carnage(player_1, hero_jelly) 
        carnage_counter = 4  
        if player_1.booty_bomb == True:
          poison_damage = random.randint(5,10)
          print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
          champ_jelly.lose_health_champ(poison_damage)  
      else:
        if player_1.axe == True:
          choice_list = ['attack', 'axe', 'run', 'potion', 'make friends']
          choice = input(f"Please type {Fore.MAGENTA}'attack', 'axe', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'.{Style.RESET_ALL}  ").lower()
          player_1.flee_chance = False
          if choice not in choice_list:
              time.sleep(0.5)
              print("Ha Ha, you're funny. Sorry, that's not an available option."  )
          elif choice == "make friends":
              time.sleep(1)
              print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} already has enough friends, unfortunately.")
              time.sleep(0.5)
              
              if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                champ_jelly.list_of_champion_attacks(player_1, hero_jelly) 
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                  time.sleep(0.5)
                  champ_jelly.champ_attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health < 50:
                  carnage_counter -= 1
                  if champ_jelly.potions != 0:
                    champ_jelly.use_potion()
                  elif champ_jelly.potions == 0:
                    champ_jelly.champ_attack(player_1, hero_jelly)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
          elif choice == "attack":
              time.sleep(0.5)
              player_1.champ_player_attack(champ_jelly)
              time.sleep(0.5)
              hero_jelly.champ_player_attack(champ_jelly, player_1)
              time.sleep(1)
              if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                  time.sleep(0.5)
                  champ_jelly.champ_attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health < 50:
                  carnage_counter -= 1
                  if champ_jelly.potions != 0:
                    champ_jelly.use_potion()
                  elif champ_jelly.potions == 0:
                    champ_jelly.champ_attack(player_1, hero_jelly)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
          elif choice == 'axe':
              time.sleep(0.5)
              player_1.champ_elemental_attack(champ_jelly)
              time.sleep(1)
              hero_jelly.champ_player_attack(champ_jelly, player_1)
              time.sleep(1)
              if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                  time.sleep(0.5)
                  champ_jelly.champ_attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health < 50:
                  carnage_counter -= 1
                  if champ_jelly.potions != 0:
                    champ_jelly.use_potion()
                  elif champ_jelly.potions == 0:
                    champ_jelly.champ_attack(player_1, hero_jelly)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
          elif choice == "potion":
              heal_list = ['p', 'h']
              heal_choice = input(f"Who will recieve the potion? Please type {Fore.MAGENTA}'p'{Style.RESET_ALL} for {Fore.CYAN}Player{Style.RESET_ALL} or {Fore.MAGENTA}'h'{Style.RESET_ALL} for {Fore.CYAN}Hero Jelly.{Style.RESET_ALL}").lower() 
              while heal_choice not in heal_list:
                heal_choice = input(f"Sorry, that is not a valid option. Please press {Fore.MAGENTA}'p'{Style.RESET_ALL} for {Fore.CYAN}Player{Style.RESET_ALL} or {Fore.MAGENTA}'h'{Style.RESET_ALL} for {Fore.CYAN}Hero Jelly.{Style.RESET_ALL}").lower()
                time.sleep(0.5)
              if heal_choice == 'p':
                player_1.use_potion()
                hero_jelly.champ_player_attack(champ_jelly, player_1)
              elif heal_choice == 'h':
                player_1.use_potion_ally(hero_jelly)
                hero_jelly.champ_player_attack(champ_jelly, player_1)
                if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                  champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                      poison_damage = random.randint(5,10)
                      print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                      champ_jelly.lose_health_champ(poison_damage)
                elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                    time.sleep(0.5)
                    champ_jelly.champ_attack(player_1, hero_jelly)
                    time.sleep(0.5)
                    champ_boss_counter += 1
                    if player_1.booty_bomb == True:
                      poison_damage = random.randint(5,10)
                      print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                      champ_jelly.lose_health_champ(poison_damage)
                elif champ_jelly.health < 50:
                    carnage_counter -= 1
                    if champ_jelly.potions != 0:
                      champ_jelly.use_potion()
                    elif champ_jelly.potions == 0:
                      champ_jelly.champ_attack(player_1, hero_jelly)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                    if player_1.booty_bomb == True:
                      poison_damage = random.randint(5,10)
                      print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                      champ_jelly.lose_health_champ(poison_damage)
          elif choice == "run":
              time.sleep(0.5)
              print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Mortifying Technique.{Style.RESET_ALL} You can't run!?!")
              if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                  time.sleep(0.5)
                  champ_jelly.champ_attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health < 50:
                  carnage_counter -= 1
                  if champ_jelly.potions != 0:
                    champ_jelly.use_potion()
                  elif champ_jelly.potions == 0:
                    champ_jelly.champ_attack(player_1, hero_jelly)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
        elif player_1.axe == False:  
          choice_list = ['attack', 'run', 'potion', 'make friends']
          choice = input(f"Please type {Fore.MAGENTA}'attack', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'.{Style.RESET_ALL}  ").lower()
          player_1.flee_chance = False
          if choice not in choice_list:
              time.sleep(0.5)
              print("Ha Ha, you're funny. Sorry, that's not an available option."  )
          elif choice == "make friends":
              time.sleep(1)
              print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} has enough friends already, unfortunately.")
              time.sleep(0.5)
              
              if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                champ_jelly.list_of_champion_attacks(player_1, hero_jelly) 
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                  time.sleep(0.5)
                  champ_jelly.champ_attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health < 50:
                  carnage_counter -= 1
                  if champ_jelly.potions != 0:
                    champ_jelly.use_potion()
                  elif champ_jelly.potions == 0:
                    champ_jelly.champ_attack(player_1, hero_jelly)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
          elif choice == "attack":
              time.sleep(0.5)
              player_1.champ_player_attack(champ_jelly)
              time.sleep(0.5)
              hero_jelly.champ_player_attack(champ_jelly, player_1)
              time.sleep(1)
              if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                  time.sleep(0.5)
                  champ_jelly.champ_attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health < 50:
                  carnage_counter -= 1
                  if champ_jelly.potions != 0:
                    champ_jelly.use_potion()
                  elif champ_jelly.potions == 0:
                    champ_jelly.champ_attack(player_1, hero_jelly)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
          elif choice == "potion":
            heal_list = ['p', 'h']
            heal_choice = input(f"Who will recieve the potion? Please type {Fore.MAGENTA}'p'{Style.RESET_ALL} for {Fore.CYAN}Player{Style.RESET_ALL} or {Fore.MAGENTA}'h'{Style.RESET_ALL} for {Fore.CYAN}Hero Jelly.{Style.RESET_ALL}").lower() 
            while heal_choice not in heal_list:
              heal_choice = input(f"Sorry, that is not a valid option. Please press {Fore.MAGENTA}'p'{Style.RESET_ALL} for {Fore.CYAN}Player{Style.RESET_ALL} or {Fore.MAGENTA}'h'{Style.RESET_ALL} for {Fore.CYAN}Hero Jelly.{Style.RESET_ALL}").lower()
              time.sleep(0.5)
            if heal_choice == 'p':
              player_1.use_potion()
              hero_jelly.champ_player_attack(champ_jelly, player_1)
            elif heal_choice == 'h':
              player_1.use_potion_ally(hero_jelly)
              time.sleep(0.5)
              hero_jelly.champ_player_attack(champ_jelly, player_1)
              if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                  time.sleep(0.5)
                  champ_jelly.champ_attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health < 50:
                  carnage_counter -= 1
                  if champ_jelly.potions != 0:
                    champ_jelly.use_potion()
                  elif champ_jelly.potions == 0:
                    champ_jelly.champ_attack(player_1, hero_jelly)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
          elif choice == "run":
              time.sleep(0.5)
              print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Mortifying Technique.{Style.RESET_ALL} You can't run!?!")
              if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
                champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                  time.sleep(0.5)
                  champ_jelly.champ_attack(player_1, hero_jelly)
                  time.sleep(0.5)
                  champ_boss_counter += 1
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
              elif champ_jelly.health < 50:
                  carnage_counter -= 1
                  if champ_jelly.potions != 0:
                    champ_jelly.use_potion()
                  elif champ_jelly.potions == 0:
                    champ_jelly.champ_attack(player_1, hero_jelly)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                  if player_1.booty_bomb == True:
                    poison_damage = random.randint(5,10)
                    print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                    champ_jelly.lose_health_champ(poison_damage)
    elif hero_jelly.is_dead == True:
      champion_loop_no_hero()                     

def champion_loop_no_hero():
  global champ_boss_counter 
  global carnage_counter 
  while player_1.health > 0 and champ_jelly.health > 0:
    if carnage_counter == 0:
      champ_jelly.carnage(player_1, hero_jelly) 
      carnage_counter = 4   
      if player_1.booty_bomb == True:
        poison_damage = random.randint(5,10)
        print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
        champ_jelly.lose_health_champ(poison_damage) 
    else:
      if player_1.axe == True:
        choice_list = ['attack', 'axe', 'run', 'potion', 'make friends']
        choice = input(f"Please type {Fore.MAGENTA}'attack', 'axe', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'.{Style.RESET_ALL}  ").lower()
        player_1.flee_chance = False
        if choice not in choice_list:
            time.sleep(0.5)
            print("Ha Ha, you're funny. Sorry, that's not an available option."  )
        elif choice == "make friends":
            time.sleep(1)
            print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} already has enough friends, unfortunately.")
            time.sleep(0.5)
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
             champ_jelly.list_of_champion_attacks(player_1, hero_jelly) 
             champ_boss_counter += 1
             if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
        elif choice == "attack":
            time.sleep(0.5)
            player_1.champ_player_attack(champ_jelly)
            
            time.sleep(1)
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
              champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
              champ_boss_counter += 1
              if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
        elif choice == 'axe':
            time.sleep(0.5)
            player_1.champ_elemental_attack(champ_jelly)
            time.sleep(1)
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
              champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
              champ_boss_counter += 1
              if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
        elif choice == "potion":
            time.sleep(0.5)
            player_1.use_potion()
            
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
             champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
             champ_boss_counter += 1
             if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
        elif choice == "run":
            time.sleep(0.5)
            print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Mortifying Technique.{Style.RESET_ALL} You can't run!?!")
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
             champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
             champ_boss_counter += 1
             if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage) 
      elif player_1.axe == False:  
        choice_list = ['attack', 'run', 'potion', 'make friends']
        choice = input(f"Please type {Fore.MAGENTA}'attack', 'run',{Style.RESET_ALL} or {Fore.MAGENTA}'potion'.{Style.RESET_ALL}  ").lower()
        player_1.flee_chance = False
        if choice not in choice_list:
            time.sleep(0.5)
            print("Ha Ha, you're funny. Sorry, that's not an available option."  )
        elif choice == "make friends":
            time.sleep(1)
            print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} has enough friends already, unfortunately.")
            time.sleep(0.5)
            
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
             champ_jelly.list_of_champion_attacks(player_1, hero_jelly) 
             champ_boss_counter += 1
             if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
        elif choice == "attack":
            time.sleep(0.5)
            player_1.champ_player_attack(champ_jelly)
            
            time.sleep(1)
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
              champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
              champ_boss_counter += 1
              if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
        elif choice == "potion":
            time.sleep(0.5)
            player_1.use_potion()
            
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
             champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
             champ_boss_counter += 1
             if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
        elif choice == "run":
            time.sleep(0.5)
            print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} uses {Fore.LIGHTGREEN_EX}Mortifying Technique.{Style.RESET_ALL} You can't run!?!")
            if champ_jelly.health >= 50 and champ_boss_counter % 3 == 1:
             champ_jelly.list_of_champion_attacks(player_1, hero_jelly)
             champ_boss_counter += 1
             if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health >= 50 and champ_boss_counter % 3 != 1:
                time.sleep(0.5)
                champ_jelly.champ_attack(player_1, hero_jelly)
                time.sleep(0.5)
                champ_boss_counter += 1
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
            elif champ_jelly.health < 50:
                carnage_counter -= 1
                if champ_jelly.potions != 0:
                  champ_jelly.use_potion()
                elif champ_jelly.potions == 0:
                  champ_jelly.champ_attack(player_1, hero_jelly)
                print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is readying {Fore.LIGHTGREEN_EX}Carnage...{Style.RESET_ALL}in {carnage_counter}...")
                if player_1.booty_bomb == True:
                  poison_damage = random.randint(5,10)
                  print(f"The {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} is {Fore.LIGHTGREEN_EX}POISONED!{Style.RESET_ALL}\nThe {Fore.LIGHTGREEN_EX}Jelly King's Champion{Style.RESET_ALL} suffers {Fore.LIGHTRED_EX}{poison_damage} HP damage.{Style.RESET_ALL}")
                  champ_jelly.lose_health_champ(poison_damage)
# Naming the player and initiating "Escape from Jelly Castle"
print("""
      Welcome to...
      
      ESCAPE FROM     
            ____  ____  __    __   _  _ 
           (_  _)( ___)(  )  (  ) ( \/ )
          .-_)(   )__)  )(__  )(__ \  / 
          \____) (____)(____)(____)(__)     

          
   .=-.-.  ,-,--.               ,---.      .-._                      
  /==/_ /,-.'-  _\   _.-.     .--.'  \    /==/ \  .-._   _,..---._   
 |==|, |/==/_ ,_.' .-,.'|     \==\-/\ \   |==|, \/ /, //==/,   -  \  
 |==|  |\==\  \   |==|, |     /==/-|_\ |  |==|-  \|  | |==|   _   _\ 
 |==|- | \==\ -\  |==|- |     \==\,   - \ |==| ,  | -| |==|  .=.   | 
 |==| ,| _\==\ ,\ |==|, |     /==/ -   ,| |==| -   _ | |==|,|   | -| 
 |==|- |/==/\/ _ ||==|- `-._ /==/-  /\ - \|==|  /\ , | |==|  '='   / 
 /==/. /\==\ - , //==/ - , ,/\==\ _.\=\.-'/==/, | |- | |==|-,   _`/  
 `--`-`  `--`---' `--`-----'  `--`        `--`./  `--` `-.`.____.'   
            
                                                   Championship Edition
""") 
time.sleep(1)
player_one_name = input(f"Please type your character name then press 'enter'.")
time.sleep(0.5)
# Creating instances
jelly_1 = Jelly()
player_1 = Player(player_one_name)
hero_jelly = HeroJelly(name="The Great Hero Jelly")
boss_jelly = BossJelly() 
champ_jelly = BossJelly(spell=True, potions=2)
player_xp = 0

print(f"Hello {player_1.name}! Please select a difficulty.")
time.sleep(0.5)
difficulty_list = ['e', 'n']
difficulty = input("If you are used to getting your way in life and want someone to hold your hand through this, press 'e' for easy;\nIf you want a decent challenge that will take you 3 or 4 playthroughs to finish, press 'n' for normal.").lower()
while difficulty not in difficulty_list:
  difficulty = input(f"Sorry, that is not a valid option. Please type 'e' for easy or 'n' for normal.")
if difficulty == 'e':
  player_1.health = 400
  player_1.ring = True
elif difficulty == 'n':
  player_1.health = 200
print("Fantastic! Let's get started!")
time.sleep(2)
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
throne_room_counter = 0
evasion_boots = True 
staff_quarters_counter = 0
staff_quarters_potion = True
royal_quarters_counter = 0
defense_ring = True
theater_counter = 0
theater_note = True
forest_entrance_potions = True
forest_entrance_counter = 0
path_to_hut_potion = True
path_to_hut_counter = 0 
forest_pond_potions = True
forest_pond_counter = 0
forest_hut_potions = True
forest_hut_counter = 0
forest_center_potion = True
forest_center_counter = 0
west_edge_potion = True
west_edge_counter = 0
northwest_corner_potion = True
northwest_corner_counter = 0
forest_cave_potions = True
forest_cave_counter = 0
drawbridge_counter = 0
meditation_active = False
meditate_counter = 3 
#Global variables
player_opposing_elements = []
player_axe_elements = []
champ_boss_counter = 0
carnage_counter = 4 
eat_cake = False 
# Game loop runs within dungeon cave
dungeon_cave()
