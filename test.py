import time
import random

class Player():                                                 #Class for the player.                                               
    def __init__(self, name, hp, xp, inventory, weapon_dm):
        self.name = name            #Player's name.
        self.hp = hp                #Player's health points (Out of 100).
        self.xp = xp                #Player's experience points (I may add a feature where the player can use these to progress further in the game).
        self.inventory = inventory  #Inventory containing the player's items.
        self.weapon_dm = weapon_dm  #Contains each weapon and the damage it deals.

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
            print("-----------------------------------------------------------------------")
            print('Your sword dealt ' + str(loss) + ' damage to ' + enemy1.name)
            print(loss)
            return self.hp
        elif userInput == 'heal_potion':
            if self.inventory['heal_potion'] >= 1:
                self.inventory['heal_potion'] -= 1
                self.hp += 20 #Restore 20 health points for the player.
                print("-----------------------------------------------------------------------")
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
                    print("-----------------------------------------------------------------------")
                    print('Your sword dealt ' + str(loss) + ' damage to ' + enemy1.name)
                    print(loss)
                    return self.hp
            else:
                print('You do not have any attack potions.')
                player1.player_turn()
        else:
            print('This item is not available in your inventory.')
            player1.player_turn()


class Enemy():                              #Class for each enemy.
    def __init__(self, name, hp, attack):
        self.name = name                    #Enemy name.
        self.hp = hp                        #Enemy's health points.
        self.attack = attack                #Damage dealt by enemy.

    def __str__(self):
        return f'{self.name}, {self.hp}, {self.attack}'
    
    def enemy_info(self):
        return self.name, self.hp, self.attack
    
    def enemy_turn(self):                   #Enemy's turn in a turn based battle.
        self.attack = random.randint(16, 24)
        player1.hp -= self.attack
        print('You have lost ' + str(self.attack) + ' from ' + str(self.name))
        print('Health: ' + str(player1.hp))


def load_data():
    print("Welcome!")
    with open("data.txt", 'r') as reader:       #Load player data from the data.txt file.
        line = reader.readlines()
        player1 = Player(line[0], int(line[1]), int(line[2]), line[3], line[4])
        enemy1 = Enemy(line[5], int(line[6]), int(line[7]))
    load_checkpoint()

def load_checkpoint():
    with open("checkpoint.txt", 'r') as reader: #Load player's most recent checkpoint from checkpoint.txt.
        line = reader.readlines()
        for i in line:
            checkpoints[int(i)]()               #This will load the first function in checkpoints which is introduction.

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
        directions["M"] = menu                            #Add an option for the menu in the directions dictionary above.
        time.sleep(2)
        print('Tip: You have enough coins to purchase a bow in the shop.')
    elif enemy1.hp >= 0 and 'bow' not in player1.inventory: #This triggers when the player has neither beaten enemy1 nor purchased a bow.
        player1.add_apple_to_inventory()
        print("-----------------------------------------------------------------------")
        print(player1.hp)
        print(list_data)
        print('Your inventory lists what items you have and the amount of each item.')
        print(player1.inventory)
        print("You found an apple on your way to the town.")

    print("You are in the center of a town. You should go East to purchase supplies.") #Program ignores previous if statements when the player has both purchased a bow and defeated enemy1.
    if enemy1.hp > 0:
        userInput = input("N = palace, E = shop, B = introduction: ")
    else:
        userInput = input("N = palace, E = shop, B = introduction, M = menu: ")
    if userInput in directions:
        directions[userInput]()
    if userInput == "M":
        menu()
    else:
        print("Enter a valid direction")
        towncenter()

def shop():
    file = open("checkpoint.txt")
    line = file.readlines()
    if line[0] == "0":
        userInput = input("Would you like to save your progress. Press 'y' if yes.")
        with open("checkpoint.txt", 'w') as checkpoint:
            if userInput == "y":
                checkpoint.write("1")
                print(checkpoint)
            checkpoint.close()
        with open("data.txt", 'w') as data:
            for i in list_data:
                data.writelines(str(i))
                data.writelines('\n')
            data.close()
        saved_checkpoint = open("checkpoint.txt").read()
        print(saved_checkpoint)
        userInput = input("Test checkpoint?. Press y to confirm.")
        if userInput == "y":
            checkpoints[int(saved_checkpoint)]()

    else:
        print("-----------------------------------------------------------------------")    
        print(player1.inventory)           
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
                print("-----------------------------------------------------------------------")
                print('Your inventory after your purchase.')
                print(player1.inventory)
                player1.inventory[userInput] = 1
                player1.weapon_dm[userInput] = 20
                print('You purchased a ' + userInput + '! Return to the town center and go to the palace to continue.')
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
    print("-----------------------------------------------------------------------")
    print("You encounter an enemy on the way to the palace.")
    if 'sword' in player1.inventory: #If the player has a sword equipped.
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
    print("-----------------------------------------------------------------------")
    print(player1.inventory)
    print('A healing potion has been added to your inventory. It will restore 20 of your hp.')

    while player1.hp >= 1 and enemy1.hp >= 1: #While loop that continues as long both the player and enemy have at least 1 health point.
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
        print("-----------------------------------------------------------------------")
        print('You defeated ' + enemy1.name + ' in battle.')
        print('You find and add 5 coins to your inventory')
        player1.inventory['coins'] += 5
        print(player1.inventory)
        player1.xp += 10
        print("You received " + str(10) + " experience points!")
        time.sleep(3)
        print('Thank you for playing the demo of this game!')
        list_data[1] = player1.hp                                   #Since player1.hp in list_data is a copy of the player's initial health (i.e. 100), it is updated with the current value of player1.hp.
        list_data[6] = enemy1.hp
        loading = 'loading'     
        for i in range(1, 4):
            print(loading)
            time.sleep(1)
        userInput = input("Would you like to save your progress? Type 'y' to confirm.")
        with open("data.txt", 'w') as data:
            for i in list_data:
                data.writelines(str(i))
                data.writelines('\n')
            data.close()
        with open("checkpoint.txt", 'w') as checkpoint:
            if userInput == "y":
                checkpoint.write("2")
                print(checkpoint)
            checkpoint.close()
        towncenter()

def menu():
    menu_options = ["RESUME", "quit", "stats", "enemy_profiles"] #Work in progress
    i = 0
    print(menu_options)
    userInput = input("Type 'left' and 'right' to navigate between the options." + '/n' + "Type 'y' to choose an option.")
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
        elif userInput == "y":
            break
    if i == 0:
        load_checkpoint()
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
    option = input("Add or remove a 0. Type two numbers to select the x and y axis. Type finish to complete character creation.")
    while option != "Finish":
        x = int(input())
        y = int(input())
        if option == "add":
            list_character_pixels[x][y] = "0"
            for i in list_character_pixels:
                print(i)
            option = input("Type 'add' to add a 0 or 'remove' to remove a 0. Type two numbers to select the x and y axis. Type finish to complete character creation.")
        elif option == "remove":
            list_character_pixels[x][y] = "*"
            for i in list_character_pixels:
                print(i)
            option = input("Type 'add' to add a 0 or 'remove' to remove a 0. Type two numbers to select the x and y axis. Type finish to complete character creation.")
        else:
            print("Not a valid command.")
            for i in list_character_pixels:
                print(i)
            option = input("Type 'add' to add a 0 or 'remove' to remove a 0. Type two numbers to select the x and y axis. Type finish to complete character creation.")

    if option == "Finish":
        string_welcome = "Welcome!"
        for i in string_welcome:
            print(i)
            time.sleep(0.5)
        print("Welcome!")

def test_checkpoint():
    current_area = [towncenter]
    userInput = input()
    if userInput == "back":
        current_area[0]()

player1 = Player('player1', 100, 0, {'coins': 3, 'attack_potion': 1}, {}) #Player instance
enemy1 = Enemy('Enemy1', 100, 15)                                         #Enemy instance
checkpoints = {0: introduction, 1: shop, 2: towncenter}                   #Programme loops over this dictionary until the key matches with the number in checkpoint.txt.
list_data = [player1.name, player1.hp, player1.xp, player1.inventory, player1.weapon_dm, enemy1.name, enemy1.hp, enemy1.attack]

load_data()