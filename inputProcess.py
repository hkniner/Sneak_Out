
'''
getUserComm:
function that checks where user is and gives them a while true loop with options on what to pick
from a list of valid commands.
It has 1 parameter: 
world - Get information of what player has done and where they are at
'''
def getUserComm(world):
    #PostGame controls
    if world["PostGame"] == True:
        validCommands = ["stats", "quit"]
        while True:
            userInput = input("Either quit or view player stats(stats, quit)\n:")
            userInput = userInput.lower().strip()
            if userInput not in validCommands:
                print("Not a valid command.")
                continue
            return userInput
    #Mini Map controls
    if world["inMap"] == True:
        validCommands = ['n', 'e', 'w', 's', 'inv']
        while True:
                userInput = input("Enter a direction (n,e,w,s) or open 'inv'\n: ")
                userInput = userInput.lower().strip()
                if userInput not in validCommands:
                    print("Not a valid command")
                    continue
                return userInput
    #Front Door controls
    if world["playerLoc"] == world["POI"]["Front Door"]:
        #Checks if in Key Game at the end 
        if world["poiFlags"]["Front Door"]["InKeyGame"]:
            validCommands = ["right", "left", "leave"]
            while True:
                    userInput = input("Which way will you turn the key?(right, left, leave)\n: ")
                    userInput = userInput.lower().strip()
                    if userInput not in validCommands:
                        print("Not a valid command")
                        continue
                    return userInput
        else:
            validCommands = ["sneakout", "leave"]
            while True:
                    userInput = input("A giant door stands in your way...It almost looks menacing\nWhat will you do?(SneakOut, leave)\n: ")
                    userInput = userInput.strip().lower()
                    if userInput not in validCommands:
                        print("Not a valid command")
                        continue
                    return userInput
    #Parents room controls
    if world["playerLoc"] == world["POI"]["Parents Room"]:
        #Checks to see if have slippers to enter room
        if "slippers" in world["player"]["inv"]:
            validCommands = ["closet", "dresser", "nightstand", "leave"]
            while True:
                    userInput = input("Where do you want to go?(closet, dresser, nightstand, leave)\n: ")
                    userInput = userInput.lower().strip()
                    if userInput not in validCommands:
                        print("Not a valid command.")
                        continue
                    return userInput
        #If doesnt have slippers, automatically kicks out
        else:
            userInput = "leave"
            return userInput
    #Your Room Controls
    if world["playerLoc"] == world["POI"]["Your Room"]:
        validCommands = ["closet", "sleep", "lookaround", "leave"]
        while True:
            userInput = input("Where do you want to go?(closet, sleep, LookAround, leave)\n:")
            userInput = userInput.lower().strip()
            if userInput not in validCommands:
                print("Not a valid command.")
                continue
            return userInput
    #Kitchen Controls
    if world["playerLoc"] == world["POI"]["Kitchen"]:
        #Checks to see if stove is still functional
        if world["Stove"] == 0:
            #Checks to see if steak is in inventory
            if "steak" in world["player"]["inv"]:
                validCommands = ["cabinet", "fridge", "eat", "leave"]
                while True:
                    userInput = input("Where do you want to go?(cabinet, fridge, eat, leave)\n:")
                    userInput = userInput.lower().strip()
                    if userInput not in validCommands:
                        print("Not a valid command.")
                        continue
                    return userInput
            else:
                validCommands = ["cabinet", "fridge", "leave"]
                while True:
                    userInput = input("Where do you want to go?(cabinet, fridge, leave)\n:")
                    userInput = userInput.lower().strip()
                    if userInput not in validCommands:
                        print("Not a valid command.")
                        continue
                    return userInput
        else:
            #Checks to see if steak is in inventory
            if "steak" in world["player"]["inv"]:
                validCommands = ["stove", "cabinet", "fridge", "eat", "leave"]
                while True:
                    userInput = input("Where do you want to go?(stove, cabinet, fridge, eat, leave)\n:")
                    userInput = userInput.lower().strip()
                    if userInput not in validCommands:
                        print("Not a valid command.")
                        continue
                    return userInput
            else:
                validCommands = ["stove", "cabinet", "fridge", "leave"]
                while True:
                    userInput = input("Where do you want to go?(stove, cabinet, fridge, leave)\n:")
                    userInput = userInput.lower().strip()
                    if userInput not in validCommands:
                        print("Not a valid command.")
                        continue
                    return userInput
'''
processUserComm():
takes a userInput and state of the world and changes a part of the player(location, death, in map or not) and returns it.
It has 3 parameters:
world - player location, hunger and stats as well to set flags, loc - change player location, userInput - see what user has done
''' 
def processUserComm(world, loc, userInput):
    #Checks to see if hunger drops to 0
    if world["player"]["hunger"] == 0:
        world["GameOver"] = True
        return world
    #Checks to see if in minimap
    if world["inMap"] == True:
        if userInput == 'e' and loc["x"] < len(world["board"])-1:
            loc["x"] += 1
            world["player"]["hunger"] -=1
            world["stats"]["Hunger Used"] +=1
        if userInput == 's' and loc["y"] < len(world["board"])-1:
            loc["y"] += 1
            world["player"]["hunger"] -=1
            world["stats"]["Hunger Used"] +=1
        if userInput == 'w' and loc["x"] > 0:
            loc["x"] -= 1
            world["player"]["hunger"] -=1
            world["stats"]["Hunger Used"] +=1
        if userInput == 'n' and loc["y"] > 0:
            loc["y"] -= 1
            world["player"]["hunger"] -=1
            world["stats"]["Hunger Used"] +=1
        if userInput == 'inv':
            printInventory(world)
    #Checks to see if at a POI
        if world["playerLoc"] == world["POI"]["Front Door"]:
            world["inMap"] = False
        if world["playerLoc"] == world["POI"]["Parents Room"]:
            world["inMap"] = False
        if world["playerLoc"] == world["POI"]["Your Room"]:
            world["inMap"] = False
        if world["playerLoc"] == world["POI"]["Kitchen"]:
            world["inMap"] = False
        return world, loc

'''
getUserName(): 
asks user to name character and returns that name
does not allow names larger than 10 char and less than 3 char
no parameters
'''
def getUserName():
    space = ' '
    while True:
        userInput = input("Enter a name for your character?\n: ")
        userInput = userInput.upper().strip()
        print(f"Nice to meet you, {userInput}.")
        #Makes it so cant use blank name and sets parameters for character count
        if userInput in space:
            print("Cannot just use a blank name.")
            continue
        if len(userInput) < 3:
            print("3 characters or more please.")
            continue
        if len(userInput) > 10:
            print("10 characters or less please.")
            continue

        return userInput
'''
printInventory(): 
takes user collected items, and throws them into one output string to see it clearly then prints string before pausing game
It has 1 parameter:
world - to see inventory items
'''

def printInventory(world):
    import time
    #Makes output string
    outputString = "[Inventory] : "
    for i in world["player"]["inv"]:
        #If item in inventory changes it into colored and adds it to output string
        if i == "slippers":
            col_op = " \033[34mSlippers\033[0m ,"
            outputString += col_op
        if i == "key":
            col_op = " \033[33mKey\033[0m ,"
            outputString += col_op
        if i == "steak":
            col_op = " \033[31mSteak\033[0m ,"
            outputString += col_op
    print(outputString)
    time.sleep(5)

'''
getStatInventory(): 
similar to printInventory but puts all items collected and doesnt remove any into one string and returns it
It has 1 parameter:
world - to see items collected
'''

def getStatInventory(world):
    count = 0
    #Makes output string
    outputString = ""
    #If item in inventory changes it into colored and adds it to output string except steak
    for i in world["stats"]["Items Collected"]:
        if i == "slippers":
            col_op = " \033[34mSlippers\033[0m ,"
            outputString += col_op
        if i == "key":
            col_op = " \033[33mKey\033[0m ,"
            outputString += col_op
        if i == "steak":
            count += 1 
    #Adds colored steak to inventory at end with count of how many obtained
    col_op = f"\033[31mSteak\033[0m x {count}"
    outputString += col_op
    return outputString

'''
getTxtInventory(): 
similar to getStatInventory but puts all items collected and doesnt remove any into one string that can
be read by a .txt file and returns it
It has 1 parameter:
world - to see items collected
'''

def getTxtInventory(world):
    count = 0
    outputString = ""
    for i in world["stats"]["Items Collected"]:
        if i == "slippers":
            col_op = " Slippers ,"
            outputString += col_op
        if i == "key":
            col_op = " Key ,"
            outputString += col_op
        if i == "steak":
            count += 1
    #Adds steak to inventory at end with count of how many obtained
    col_op = f" Steak x {count}"
    outputString += col_op
    return outputString
    
    