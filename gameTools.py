import random
from inputProcess import *
'''
setColor():
asks user for choice of valid colors and outputs a string to that color of choice
It takes 2 parameters:
color - string that needs to be in valid_Colors, string - any piece of text that user wants changed
'''

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

'''
getColor():
similar to setColor()
asks user for choice of valid colors and outputs the color chosen in a string
It takes no parameters
'''

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

'''
dndDiceRoll():
Takes a string and rolls a user set number of dices that have a user set number of sides and returns results in a list.
It has 1 parameter:
dstr - a string that is formatted as "xdy" x being the number of dice and y being the number of sides - d is always d
'''
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

'''
createPlayer():
creates a player based on user information given and throws it all into a dictionary for the player
some include name(color), name(plain), user color, max hunger and current hunger and the player inventory
It has no parameters.
'''

def createPlayer():
    player = {
    }
    player["name"] = getUserName()
    player["txtName"] = player["name"]
    player["color"] = getColor()
    player["name"] = setColor(player["color"], player["name"])
    maxhunger = dndDiceRoll("10d2")
    player["maxHung"] = sum(maxhunger)
    player["hunger"] = player["maxHung"]
    player["inv"] = []
    return player

'''
printHunger():
takes the current hunger of the player and multiplys it into a star count and
prints a counter that shows the current hunger level.
It takes 1 parameter:
world - to see the current player hunger
'''

def printHunger(world):
    starct = world["player"]["hunger"] * "*"
    output_string = "[Hunger] :" + starct
    print(output_string)

'''
processStats():
takes all different statistics from player and adds it to an output string to be seen in a more orderly fashion
It takes 1 parameter:
world - to see player stats
'''

def processStats(world):
    outputString = " "
    dashct = 21 - ((len(world["player"]["name"]) - 11) + 5)
    dashstr = dashct * "-"
    outputString +=(f"\n---------{world["player"]["name"]}" + f"{dashstr}\n")
    outputString += f"{world["stats"]["Date of Creation"]}\n"
    outputString += f"Name: {world["player"]["name"]}\n"
    outputString += f"Time played: {world["stats"]["Time Played"]}\n"
    outputString += f"# of Cycles: {world["stats"]["Cycle Count"]}\n"
    outputString += f"Hunger used: {world["stats"]["Hunger Used"]}\n"
    outputInv = getStatInventory(world)
    outputString += f"Items Collected: {outputInv}\n"
    outputString += "-------------------------\n"
    return outputString

def processTxtStats(world):
    outputString = " "
    dashct = 21 - ((len(world["player"]["name"]) - 11) + 5)
    dashstr = dashct * "-"
    outputString += (f"\n---------{world["player"]["txtName"]}" + f"{dashstr}\n")
    outputString += f"{world["stats"]["Date of Creation"]}\n"
    outputString += f"Name: {world["player"]["txtName"]}\n"
    outputString += f"Time played: {world["stats"]["Time Played"]}\n"
    outputString += f"# of Cycles: {world["stats"]["Cycle Count"]}\n"
    outputString += f"Hunger used: {world["stats"]["Hunger Used"]}\n"
    outputInv = getTxtInventory(world)
    outputString += f"Items Collected: {outputInv}\n"
    outputString += "-------------------------\n"
    return outputString
