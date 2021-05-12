# cyrus gonzalez
# player classes for battle

import random
import time
import sys

# weapons list
weaponList = ["AX", "SWORD", "CLUB"]

# create player classes
class Player:
    def __init__(self, name):
        self.health = 250
        self.name = name

# create attack decisions
    def attack(self):
        if weapon == 1:
            attackP = axAtt()
            return attackP
        elif self.weapon == 2:
            attackP = swordAtt()
            return attackP
        elif self.weapon == 3:
            attackP = clubAtt()
            return attackP

# create attack decision amounts
def chooseAttack():
    print("Which weapon would you like? ")
    choice = int(input("Ax (input 1), Sword (input 2), Club (input 3): "))
    while choice != [1,2,3]:
        if choice == 1:
            weapon = weaponList[0]
            dmg = axAtt()
        elif choice == 2:
            weapon = weaponList[1]
            dmg = swordAtt()
        elif choice == 3:
            weapon = weaponList[2]
            dmg = clubAtt()
        else:
            print("Choose a correct weapon number.")
            choice = int(input("Ax (input 1), Sword (input 2), Club (input 3): "))

        return dmg

# name the players
player1 = Player("Red Warrior")
player2 = Player("Blue Warrior")

## ax damage does 20-50 DPS (5% CRT/15% miss)
def axAtt():
    dam = random.randint(20, 45)
    cri = random.randint(45, 75)
    crit = random.randint(-5, 30)
    if crit > 3:
        dam = dam
    elif crit <= 3 and crit > 0:
        print("A Crtical Hit!!")
        dam = cri
    else:
        print("It was a miss!")
        dam = 0

    return dam
    
## sword damage does 10-25 DPS (50% CRT/13% miss)
def swordAtt():
    dam = random.randint(10, 25)
    cri = random.randint(25, 50)
    crit = random.randint(-1, 5)
    if crit > 2:
        dam = dam
    elif crit <= 2 and crit >= 0:
        print("A Crtical Hit!!")
        dam = cri
    else:
        print("It was a Miss!")
        dam = 0

    return dam

## club damage does 15-40 DPS (15% CRT/10% miss)
def clubAtt():
    dam = random.randint(15,35)
    cri = random.randint(40,60)
    crit = random.randint(-10,100)
    if crit > 15:
        dam = dam
    elif crit <= 15 and crit > 0:
        print("A Crtical Hit!!")
        dam = cri
    else:
        print("It was a Miss!")
        dam = 0
        
    return dam

def main():

    gameplay = True
    # plays game function
    while gameplay:
        # prints opening
        print("Prepare to battle to the death!!!")
        print("Fight between", player1.name, "and", player2.name)
        print("Each player starts off with 250 HP,")
        print("and the HP will be displayed after each turn!")
        print("Good luck you two!")
        time.sleep(2)
        print("Ready?")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1.")
        time.sleep(1)
        print("FIGHT!")

        #set game loop in health indentities
        while (player1.health > 0 or player2.health > 0):

            # set turn basis
            playerTurn = random.randint(1,2)
            
            flag = True
            while flag:

                if playerTurn == 1:
                    print(player1.name, "Choose your attack!")
                    player1.attack = int(chooseAttack())
                    print(player1.name, "did", player1.attack, "damage to", player2.name,"!")
                    player2.health -= player1.attack
                    print(player2.name, "has", player2.health, "left!")
                    print()
                    time.sleep(2)
                    if player2.health <= 0:
                        print("We have a winner!!!")
                        print("RED WARRIOR WINS")
                        
                        flag = False
                    else:
                        continue

                elif playerTurn == 2:
                    print(player2.name, "Choose your attack!")
                    player2.attack = int(chooseAttack())
                    print(player2.name, "did", player2.attack, "damage to", player1.name,"!")
                    player1.health -= player2.attack
                    print(player1.name, "has", player1.health, "left!")
                    print()
                    time.sleep(2)
                    if player1.health <= 0:
                        print("We have a winner!!!")
                        print("BLUE WARRIOR WINS")
                        
                        flag = False
                    else:
                        continue

            gameplay = input("Do you want to fight again? (yes or no)? ")
            while gameplay != "yes" or gameplay != "1":
                if gameplay == "yes" or gameplay == "1":
                    gameplay = True
                    main()
                elif gameplay == "no" or gameplay == "2":            
                    gameplay = False
                    print("The End")
                    sys.exit()
                else:
                    print("ERROR: PICK YES OR NO.")
                    gameplay = input()

if __name__=="__main__":
    main()
