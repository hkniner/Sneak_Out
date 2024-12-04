

'''
getUserComm:
while True loop that waits for a N E W S to be put into the terminal and returns it
1 parameter, world
'''
def getUserComm(world):
    #Mini Map controls
    if world["inMap"] == True:
        validCommands = ['n', 'e', 'w', 's']
        while True:
                userInput = input("Enter a direction(n,e,w,s): ")
                userInput = userInput.lower().strip()
                if userInput not in validCommands:
                    print("Not a valid command")
                    continue
                return userInput
    #Front Door controls
    if world["playerLoc"] == world["POI"]["Front Door"]:
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
    if world["playerLoc"] == world["POI"]["Parents Room"]:
        if "slippers" in world["player"]["inv"]:
            validCommands = ["closet", "dresser", "nightstand", "leave"]
            while True:
                    userInput = input("Where do you want to go?(closet, dresser, nightstand, leave)\n: ")
                    userInput = userInput.lower().strip()
                    if userInput not in validCommands:
                        print("Not a valid command")
                        continue
                    return userInput
        else:
            userInput = "leave"
            return userInput
             

        
    
def processUserComm(world, loc, userInput):
    #Checks to see if in minimap
    if world["inMap"] == True:
        if userInput == 'e' and loc["x"] < len(world["board"])-1:
            loc["x"] += 1
        if userInput == 's' and loc["y"] < len(world["board"])-1:
            loc["y"] += 1
        if userInput == 'w' and loc["x"] > 0:
            loc["x"] -= 1
        if userInput == 'n' and loc["y"] > 0:
            loc["y"] -= 1
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
getUserName: 
asks user to name character
returns that name
does not allow names larger than 12 char
'''
def getUserName():
    space = ' '
    while True:
        userInput = input("Enter a name for your character?\n: ")
        userInput = userInput.upper().strip()
        print(f"Nice to meet you, {userInput}.")
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