current_area = []

class Player():
    def __init__(self, name, hp, inventory, weapons):
        self.name = name
        self.hp = hp
        self.inventory = inventory
        self.weapons = weapons

    def __str__(self):
        return f'{self.name}, {self.hp}, {self.inventory}, {self.weapons}'
    
    def myfunc(self):
        return self.name, self.hp, self.inventory, self.weapons

    def lesshp(self):
        self.hp -= 20
        return self.hp

    def add_apple_to_inventory(self):
        self.inventory['apple'] = 1
        return self.inventory

    def add_to_inventory(self):
        userInput = input()
        self.inventory[userInput] = 1
        print(userInput + ' added to inventory.')
        return self.inventory

    def add_to_weapons(self):
        userInput = input()
        self.weapons[userInput] = 20
        print(userInput + ' added to weapons.')
        return self.weapons
    
    def player_turn(self):
        userInput = input('Choose a weapon to use for your turn.')
        if userInput in self.weapons:
            loss = self.weapons[userInput]
            enemy1.hp -= loss
            print('Your sword dealt ' + str(loss) + ' damage to ' + enemy1.name)
            print(loss)
            return self.hp
        elif userInput == 'heal_potion':
            if self.inventory['heal_potion'] >= 1:
                self.inventory['heal_potion'] -= 1
                self.hp += 20
                print('You receive 20 hp from the potion.')
                print(self.hp)
            else:
                print('You do not have any heal potions.')
                player1.player_turn()
        elif userInput == 'attack_potion':
            if self.inventory['attack_potion'] >= 1:
                self.inventory['attack_potion'] -= 1
                print('The damage from your chosen weapon is doubled.')
                userInput = input('Choose a weapon to use for your turn.')
                if userInput in self.weapons:
                    loss = self.weapons[userInput] * 2
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
    
    def enemy_turn(self):
        player1.hp -= self.attack
        print('You have lost ' + str(self.attack) + ' from ' + str(self.name))
        print('Health: ' + str(player1.hp))


player1 = Player('player1', 100, {'coins': 3, 'attack_potion': 1}, {})
enemy1 = Enemy('Enemy1', 100, 15)

#Introduction
def introduction():
        print("You wake up to find yourself in a forest. You decide to travel North towards a town.")
        userInput = input("N = North, E = East, W = West, S = South: ")
        directions = {
            "N": towncenter,
            }
        if userInput in directions:
            directions[userInput]() # Directions dictionary above contains keys and values for the functions that neighbour the current function.
        else:
            print("I literally said you can only go North !!!!, you deserve to start again now")
            introduction()

def towncenter():
    if enemy1.hp == 0 and 'bow' not in player1.inventory:
        print('Tip: You have enough coins to purchase a bow in the shop.')
    elif enemy1.hp >= 0 and 'bow' not in player1.inventory:
        player1.add_apple_to_inventory()
        print('Your inventory lists what items you have and the amount of each item.')
        print(player1.inventory)
        print("You found an apple on your way to the town.")

    print("You are in the center of a town. You should go East to purchase supplies.")
    userInput = input("N = palace, E = shop, B = introduction: ")
    directions = {
        "N": palace,
        "E": shop,
        "B": introduction
        }
    if userInput in directions:
        directions[userInput]()
    else:
        print("Enter a valid direction")
        towncenter()

def shop():
    shop_items = {'bow': 4, 'sword': 2}
    print("What would you like to purchase?")
    print('Or press W to return to the town center')
    userInput = input("bow: 4 coins, sword: 2 coins ")
    if userInput in shop_items:
        if player1.inventory['coins'] >= shop_items[userInput]:
            player1.inventory['coins'] -= shop_items[userInput]
            print('Your inventory after your purchase.')
            print(player1.inventory)
            player1.weapons[userInput] = 20
            player1.inventory[userInput] = 1
            print('You purchased a ' + userInput)
            print(player1.weapons)
            print('The weapons dictionary indicates the effect of each weapon from your inventory.')
            shop()
        else:
            print("You do not have enough coins.")
            shop()

    elif userInput == "W":
        towncenter()
            
    else:
        print("Not a valid command")
        shop()

def palace():
        print("You encounter an enemy on the way to the palace.")
        if 'sword' in player1.weapons:
            player1.lesshp()
            print("You defeat the enemy.")
            print("Health:",player1.hp)
            print(player1.weapons)
            upstairs()
        else:
            print("Without a weapon you are killed.")
            player1.hp -= 100
            print("Health:",player1.hp)

def upstairs():
    print('You encounter a particularly difficult enemy')
    print('You find a potion that may be useful for the battle. Type heal_potion to add this item to your inventory.')
    player1.add_to_inventory()
    print(player1.inventory)
    print('A healing potion has been added to your inventory. It will restore 20 of your hp.')
    while player1.hp and enemy1.hp >= 1:
        print(player1.weapons)
        player1.player_turn()
        print('Enemy1 has ' + str(enemy1.hp) + ' hp remaining.')
        print(enemy1.name + ' attacks.')
        enemy1.enemy_turn()

    
    if player1.hp <= 1:
        print('You have been killed by ' + enemy1.name + ' in battle.')

    elif enemy1.hp <= 1:
        print('You defeated ' + enemy1.name + ' in battle.')
        print('You find and add 5 coins to your inventory')
        player1.inventory['coins'] += 5
        print(player1.inventory)
        print('Plot to be continued.')
        towncenter()

introduction() #First function call used when testing the whole game.