import random
from inputProcess import *

def dndDiceRoll(dstr):
    rolls = []
    try:
        x, y = dstr.split('d')
        x = int(x) #num of dice
        y = int(y) #num of sides

        if x <= 0 or y <= 0:
            print("Invalid input. Both x and y should be positive integers.")
    except SyntaxError:
        print("Data must be a string")
        return "null"
    except:
        print("An unexpected error occured.")
        return rolls

    for i in range(x):
        randNum = random.randint(1, y)
        rolls.append(randNum)
    return rolls

def createPlayer():
    player = {
    }
    player["name"] = getUserName()
    maxhpsum = dndDiceRoll("5d4")
    player["maxhp"] = sum(maxhpsum)
    player["hp"] = player["maxhp"]
    return player

def setColor(color, string):
    valid_Colors = ["red", "green", "yellow", "blue"]

    try:
        if color.lower().strip() in valid_Colors:
        
            ESC = "\033["
            RED = ESC + "31m"
            GREEN = ESC + "32m"
            YELLOW = ESC + "33m"
            BLUE = ESC + "34m"
            RESET = ESC + "0;0m" 

            if color.lower().strip() == "RED".lower().strip():
                color = RED
            if color.lower().strip() == "GREEN".lower().strip():
                color = GREEN
            if color.lower().strip() == "YELLOW".lower().strip():
                color = YELLOW
            if color.lower().strip() == "BLUE".lower().strip():
                color = BLUE

            clrString = color + string + RESET

            return clrString
        else:
            print("Invalid Color.")
            return string
    except:
        print("An Unexpected Error Occured.")
        return string



    

def main():
    player = createPlayer()
    print(player)
    drList1 = dndDiceRoll("10d1")
    print(drList1)
    drList2 = dndDiceRoll("20d5")
    print(drList2)
    drList3 = dndDiceRoll("5x5")
    print(drList3)
    colString = setColor("RED", "Hello World")
    print(colString)
    colString2 = setColor("PURPLE", "Testing")
    print(colString2)



main()
