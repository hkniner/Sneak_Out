'''
getUserDir:
while True loop that waits for a N E W S to be put into the terminal and returns it
no parameters
'''
def getUserDir():
    
    validCommands = ['n', 'e', 'w', 's']
    while True:
        userInput = input("Enter a direction(n,e,w,s): ")
        userInput = userInput.lower().strip()
        if userInput not in validCommands:
            print("Not a valid command")
            continue
        return userInput
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
        if userInput in space:
            print("Cannot just use a blank name.")
            continue
        if len(userInput) < 4:
            print("4 characters or more please.")
            continue
        if len(userInput) > 12:
            print("12 characters or less please.")
            continue

        return userInput