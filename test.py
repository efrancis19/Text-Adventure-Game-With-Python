import time
import random

class Player():
    def __init__(self, name, hp, xp, inventory, weapon_dm):
        self.name = name
        self.hp = hp
        self.xp = xp
        self.inventory = inventory
        self.weapon_dm = weapon_dm

    def __str__(self):
        return f'{self.name}, {self.hp}, {self.xp} {self.inventory}, {self.weapon_dm}'
    
    def myfunc(self):
        return self.name, self.hp, self.xp, self.inventory, self.weapon_dm

    def lesshp(self): #Remove 20 health points from the player.
        self.hp -= 20
        return self.hp

    def add_apple_to_inventory(self): #Add an apple to the player's inventory.
        self.inventory['apple'] = 1
        return self.inventory

    def add_to_inventory(self): #General function to add an item to the player's inventory.
        userInput = input()
        self.inventory[userInput] = 1
        return self.inventory
    
    def player_turn(self): #Player's turn during a turn based battle.
        print(player1.weapon_dm)
        userInput = input('Choose a weapon to use for your turn. You can also choose a potion if you have any available.')
        if userInput in self.weapon_dm: #If input is in both dictionaries. This ensures that items such as heal potions do not match this statement since they do not deal damage.
            loss = self.weapon_dm[userInput]
            enemy1.hp -= loss #Health points lost by the enemy equal the damage dealt by the weapon specified in the player's input. 
            print('Your sword dealt ' + str(loss) + ' damage to ' + enemy1.name)
            print(loss)
            return self.hp
        elif userInput == 'heal_potion':
            if self.inventory['heal_potion'] >= 1:
                self.inventory['heal_potion'] -= 1
                self.hp += 20 #Restore 20 health points for the player.
                print('You receive 20 hp from the potion.')
                print(self.hp)
            else:
                print('You do not have any heal potions.')
                player1.player_turn()
        elif userInput == 'attack_potion':
            if self.inventory['attack_potion'] >= 1:
                self.inventory['attack_potion'] -= 1
                print('The damage from your chosen weapon is doubled.')
                userInput = input('Choose a weapon to use for your turn. It\'s damage is doubled for this turn.')
                if userInput in self.inventory:
                    loss = self.weapon_dm[userInput] * 2 #Double the damage of the chosen weapon.
                    enemy1.hp -= loss
                    print('Your sword dealt ' + str(loss) + ' damage to ' + enemy1.name)
                    print(loss)
                    return self.hp
            else:
                print('You do not have any attack potions.')
                player1.player_turn()
        else:
            print('This item is not available in your inventory.')
            player1.player_turn()

class Enemy():
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def __str__(self):
        return f'{self.name}, {self.hp}, {self.attack}'
    
    def enemy_info(self):
        return self.name, self.hp, self.attack
    
    def enemy_turn(self): #Enemy's turn in a turn based battle.
        self.attack = random.randint(15, 23)
        player1.hp -= self.attack
        print('You have lost ' + str(self.attack) + ' from ' + str(self.name))
        print('Health: ' + str(player1.hp))


player1 = Player('player1', 100, 0, {'coins': 3, 'attack_potion': 1, 'sword': 1}, {}) #Player instance
enemy1 = Enemy('Enemy1', 100, 15) #Enemy instance

def introduction(): #Introduction Area
        print("You wake up to find yourself in a forest. You decide to travel North towards a town.")
        print("Enter a direction to move to another location(e.g. N to travel North).")
        userInput = input("N = North, E = East, W = West, S = South: ")
        directions = {
            "N": towncenter,
            }
        if userInput in directions:
            directions[userInput]() # Directions dictionary above contains keys and values for the functions that neighbour the current function.
        else:
            print("I know that I provided several directions, but this time you can only travel North.")
            introduction()

def towncenter():
    directions = {
        "N": palace,
        "E": shop,
        "B": introduction
        }
    if enemy1.hp == 0 and 'bow' not in player1.inventory: #This string triggers when the player has defeated enemy1 but has yet to purchase a bow.
        print("You can access the pause menu by typing 'M' from the town center to manage your stats.")
        directions["M"] = menu
        time.sleep(2)
        print('Tip: You have enough coins to purchase a bow in the shop.')
    elif enemy1.hp >= 0 and 'bow' not in player1.inventory: #This triggers when the player has neither beaten enemy1 nor purchased a bow.
        player1.add_apple_to_inventory()
        print('Your inventory lists what items you have and the amount of each item.')
        print(player1.inventory)
        print("You found an apple on your way to the town.")

    print("You are in the center of a town. You should go East to purchase supplies.") #Program ignores previous if statements when the player has both purchased a bow and defeated enemy1.
    userInput = input("N = palace, E = shop, B = introduction: ")
    if userInput in directions:
        directions[userInput]()
    elif userInput == "M":
        print("How did you know there was a menu option? You're not supposed to know that yet!") #A secret Easter egg.
        userInput = input("N = palace, E = shop, B = introduction: ")
    else:
        print("Enter a valid direction")
        userInput = input("N = palace, E = shop, B = introduction: ")

def shop():
    shop_items = {"blades": 4, "bow": 4, "sword": 2} #Items available in the shop.
    list_items = ["BLADES", "bow", "sword"]          #Menu for navigating between shop items.
    i = 0
    print(list_items)
    print("Select an item to purchase. Navigate by typing 'left' or 'right'. The item in uppercase indicates the item you are highlighting. Type the name of the item in lowercase to confirm your choice.")
    print('Or press W to return to the town center')
    userInput = input("blades: 4 coins, bow: 4 coins, sword: 2 coins ")
    while userInput == "left" or "right":           #While the user has not chosen an item.
        if userInput == "left":                     #User navigates left.
            list_items[i] = list_items[i].lower()   #Previously highlighted item reverted to lowercase. I index decreases by 1 to indicate movement left.
            i -= 1
            list_items[i] = list_items[i].upper()   #Newly highlighted item changed to uppercase.
            print(list_items)
            userInput = input()
        elif userInput == "right":                  #User navigates left.
            list_items[i] = list_items[i].lower()   #Previously highlighted item reverted to lowercase. I index decreases by 1 to indicate movement left.
            i += 1
            list_items[i] = list_items[i].upper()   #Newly highlighted item changed to uppercase.
            print(list_items)
            userInput = input()
        else:
            break                                   #End loop once player has confirmed their choice.
    if userInput in shop_items:                                 #If the item specified by the player is contained in the shop.
        if player1.inventory['coins'] >= shop_items[userInput]: #If the player's number of coins is greater than or equal to the number of coins for the item specified.
            player1.inventory['coins'] -= shop_items[userInput] #Decrease the value for the 'coins' key by the value of the key from the shop that was specified in the user's input.
            print('Your inventory after your purchase.')
            print(player1.inventory)
            player1.inventory[userInput] = 1
            player1.weapon_dm[userInput] = 20
            print('You purchased a ' + userInput + '! Return to the town center and go to the palace to continue')
            print(player1.inventory)
            shop()
        else: #If the player does not have enough coins.
            print("You do not have enough coins.")
            shop()

    elif userInput == "W":
        towncenter()
            
    else:
        print("Not a valid command")
        shop()

def palace():
        print("You encounter an enemy on the way to the palace.")
        if 'sword' in player1.inventory: #If the player has a sword equipped.
            player1.lesshp() #Player loses 20 health points but survives.
            print("You defeat the enemy.")
            print("Health:",player1.hp)
            print(player1.inventory)
            upstairs()
        else: #If the player does not have a sword equipped.
            print("Without a weapon you are killed.")
            player1.hp -= 100 #Player is killed and loses all of their health points.
            print("Health:",player1.hp) #No function is called and the programme ends.

def upstairs():
    print('You encounter a particularly difficult enemy.')
    print('You find a potion that may be useful for the battle. Type heal_potion to add this item to your inventory.')
    player1.add_to_inventory() #Add heal_potion to the player's inventory.
    print(player1.inventory)
    print('A healing potion has been added to your inventory. It will restore 20 of your hp.')
    while player1.hp and enemy1.hp >= 1: #While loop that continues as long both the player and enemy have at least 1 health point.
        player1.player_turn() #Call the class method that triggers the player's turn.
        print('Enemy1 has ' + str(enemy1.hp) + ' hp remaining.')
        print(enemy1.name + ' attacks.')
        enemy1.enemy_turn() #Call the class method that triggers the enemy's turn.

    
    if player1.hp <= 1:
        print('You have been killed by ' + enemy1.name + ' in battle.')
        player1.hp = 80
        enemy1.hp = 100
        upstairs() #May need a separate function to add the healing potion to prevent a player having many such potions if they're not using them in battle.

    elif enemy1.hp <= 1:
        print('You defeated ' + enemy1.name + ' in battle.')
        print('You find and add 5 coins to your inventory')
        player1.inventory['coins'] += 5
        print(player1.inventory)
        player1.xp += 10
        print("You received " + str(10) + " experience points!")
        time.sleep(3)
        print('Thank you for playing the demo of this game!')
        loading = 'loading'     
        for i in range(1, 4):
            print(loading)
            time.sleep(1)
        towncenter()

def menu():
    menu_options = ["RESUME", "quit", "stats", "enemy_profiles"] #Work in progress
    i = 0
    print(menu_options)
    userInput = input()
    while userInput == "left" or "right":           
        if userInput == "left":                     
            menu_options[i] = menu_options[i].lower()
            i -= 1
            menu_options[i] = menu_options[i].upper()
            print(menu_options)
            userInput = input()
        elif userInput == "right":                  
            menu_options[i] = menu_options[i].lower()
            i += 1
            menu_options[i] = menu_options[i].upper()
            print(menu_options)
            userInput = input()
        else:
            break
    if i == 0:
        towncenter()
    elif i == 1:
        print("Thank you for playing!")
    elif i == 2:
        print("No content available yet for this option")
        stats()
    elif i == 3:
        print("No content available yet for this option")
        menu()

def stats():
    print("Welcome to the stats section!")

def beta(): #Used to test possible future features.
    print("Beta character creator")
    list_character_pixels = [["*", "0", "*", "0", "*"], ["*", "*", "*", "*", "*"], 
                            ["0", "*", "*", "*", "0"], ["*", "0", "0", "0", "*"]]
    i = 0
    j = 0
    x = int(input())
    y = int(input())
    option = input("You can add or remove a 0. Type 'Finish' to complete character creation.")
    while option != "Finish":
        if option == "add":
            list_character_pixels[x][y] = "0"
            for i in list_character_pixels:
                print(i)
            option = input("You can add or remove a 0. Type 'Finish' to complete character creation.")
        elif option == "remove":
            list_character_pixels[x][y] = "*"
            for i in list_character_pixels:
                print(i)
            option = input("You can add or remove a 0. Type 'Finish' to complete character creation.")
        else:
            print("Not a valid command.")
            for i in list_character_pixels:
                print(i)
            option = input("You can add or remove a 0. Type 'Finish' to complete character creation.")

    if option == "Finish":
        string_welcome = "Welcome!"
        for i in string_welcome:
            print(i)
            time.sleep(0.5)
        print("Welcome!")


introduction() #First function call used when testing the whole game.