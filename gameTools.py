import random
from inputProcess import *

def setColor(color, string):
    valid_Colors = ["red", "green", "yellow", "blue", "purple", "none"]

    try:
        if color.lower().strip() in valid_Colors:
        
            ESC = "\033["
            RED = ESC + "31m"
            GREEN = ESC + "32m"
            YELLOW = ESC + "33m"
            BLUE = ESC + "34m"
            PURPLE = ESC + "35m"
            RESET = ESC + "0;0m" 

            if color.lower().strip() == "RED".lower().strip():
                color = RED
            if color.lower().strip() == "GREEN".lower().strip():
                color = GREEN
            if color.lower().strip() == "YELLOW".lower().strip():
                color = YELLOW
            if color.lower().strip() == "BLUE".lower().strip():
                color = BLUE
            if color.lower().strip() == "NONE".lower().strip():
                color = RESET
            if color.lower().strip() == "PURPLE".lower().strip():
                color = PURPLE

            clrString = color + string + RESET

            return clrString
        else:
            print("Invalid Color.")
            return string
    except:
        print("An Unexpected Error Occured.")
        return string

def getColor():
    #List of valid colors
    valid_Colors = ["red", "green", "yellow", "blue", "none"]

    #Getting color input with a True loop
    while True:
        color = input("What is your favorite color?\n(Choices: red, green, blue, yellow, none)\n: ")
        if color in valid_Colors:
            ESC = "\033["
            RED = ESC + "31m"
            GREEN = ESC + "32m"
            YELLOW = ESC + "33m"
            BLUE = ESC + "34m"
            RESET = ESC + "0;0m" 

            if color.lower().strip() == "RED".lower().strip():
                colorChoice = "RED"
            if color.lower().strip() == "GREEN".lower().strip():
                colorChoice = "GREEN"
            if color.lower().strip() == "YELLOW".lower().strip():
                colorChoice = "YELLOW"
            if color.lower().strip() == "BLUE".lower().strip():
                colorChoice = "BLUE"
            if color.lower().strip() == "NONE".lower().strip():
                colorChoice = "NONE"
            return colorChoice
        else:
            print("Invalid Color.")
            continue
    
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
    player["color"] = getColor()
    player["name"] = setColor(player["color"], player["name"])
    maxhunger = dndDiceRoll("6d2")
    player["maxHung"] = sum(maxhunger)
    player["hunger"] = player["maxHung"]
    return player

def printHunger(world):
    starct = world["player"]["hunger"] * "*"
    output_string = "[Hunger] :" + starct
    print(output_string)



