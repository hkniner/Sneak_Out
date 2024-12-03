'''
getUserComm:
while True loop that waits for a N E W S to be put into the terminal and returns it
1 parameter, world
'''
def getUserComm(world):
    
    validCommands = ['n', 'e', 'w', 's']
    while True:
        if world["inMap"] == True:
            userInput = input("Enter a direction(n,e,w,s): ")
            userInput = userInput.lower().strip()
            if userInput not in validCommands:
                print("Not a valid command")
                continue
            return userInput
    
def processUserComm(world, loc, userInput):
    if world["inMap"] == True:
        if userInput == 'e' and loc["x"] < len(world["board"])-1:
            loc["x"] += 1
        if userInput == 's' and loc["y"] < len(world["board"])-1:
            loc["y"] += 1
        if userInput == 'w' and loc["x"] > 0:
            loc["x"] -= 1
        if userInput == 'n' and loc["y"] > 0:
            loc["y"] -= 1
        return loc

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