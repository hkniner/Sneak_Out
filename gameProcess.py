from inputProcess import *
from fileProcess import *
from gameTools import *

#Colors for dialouge purposes
SLIPPERS = setColor("blue", "SLIPPERS")
KEY = setColor("yellow", "KEY")
STEAK = setColor("red", "STEAK")

def printYOUColor(world):
    YOU = setColor(world["player"]["color"],"YOU")
    return YOU


'''
printFrontDoor:
Checks for certain flags and uses the userInput to give certain text and flags back to the world
It takes 2 parameters:
A world - see where everything is and where the player is at in the game, userInput - make choices based on users Input.
'''

#FRONT DOOR PRINT
def printFrontDoor(world, userInput):
    import time
    #Detail text and leaving room
    if userInput.lower().strip() == "leave":
        print(f"{printYOUColor(world)} leave the daunting door as your want for freedom grows.\n")
        world["playerLoc"]["x"] = 3
        world["playerLoc"]["y"] = 1
        world["inMap"] = True
        return world
    #One option on what to do here: sneakout
    if userInput.lower().strip() == "sneakout":
        #Checks to see if have key and want to sneakout

        if world["poiFlags"]["Front Door"]["Unlock"] == True:
            print(f"\nAs {printYOUColor(world)} approached the door and grabbed on the doorknob, you paused waiting for your freedom...")
            time.sleep(4)
            print(f"{printYOUColor(world)} jostled the door...")
            time.sleep(3)
            print(f"{printYOUColor(world)} try to open it...\n")

            #Key Game
            
            while True:
                world["poiFlags"]["Front Door"]["InKeyGame"] = True
                count = 0
                for i in range(1,5):

                    #Check if done then returns result

                    if i == 4:
                        if count == 3:
                            #Final cutscene
                            print("\nThe Door is now Unlocked!")
                            time.sleep(3)
                            print(f"{printYOUColor(world)} step outside as the warm breeze hits your face.")
                            time.sleep(3)
                            print("What now?")
                            time.sleep(3)
                            print("\nTHE END.\n")
                            time.sleep(3)
                            #Setting flags, not in keygame and game is finished teleporting to PostGame
                            world["poiFlags"]["Front Door"]["Finish"] = True
                            world["poiFlags"]["Front Door"]["InKeyGame"] = False
                            return world
                        else:
                            print(f"\n{printYOUColor(world)} jostled the door knob more and more but...")
                            print("Its still locked.\n")
                            world["poiFlags"]["Front Door"]["InKeyGame"] = False
                            return world
                    correct_combo = ["ph", "right", "right", "left"]
                    userInput = getUserComm(world)

                    #Checks to see if individual response correct then adds something to list
                    if userInput == "leave":
                        print(f"\n{printYOUColor(world)} jostled the door knob more and more but...")
                        print("Its still locked.\n")
                        world["poiFlags"]["Front Door"]["InKeyGame"] = False
                        return world
                    if i == 1 and userInput == correct_combo[i]:
                        count += 1
                        continue
                    if i == 2 and userInput == correct_combo[i]:
                        count += 1
                        continue
                    if i == 3 and userInput == correct_combo[i]:
                        count += 1
                        continue

        if "key" not in world["player"]["inv"]:
            print(f"\nAs {printYOUColor(world)} approached the door and grabbed on the doorknob, {printYOUColor(world)} paused waiting for your freedom...")
            time.sleep(4)
            print(f"{printYOUColor(world)} jostled the door...")
            time.sleep(3)
            print("It's locked.\n")
            time.sleep(1)
            return world
        if "key" in world["player"]["inv"]:
            print(f"\nAs {printYOUColor(world)} approached the door and grabbed on the doorknob, {printYOUColor(world)} paused waiting for your freedom...")
            time.sleep(4)
            print(f"{printYOUColor(world)} jostled the door...")
            time.sleep(3)
            print("It's not locked, but as another failsafe, your annoying parents made a combination, there's a certain combination to turn the key.")
            print("(Return to this area to try a combination.)\n")
            time.sleep(1)
            world["poiFlags"]["Front Door"]["Unlock"] = True
            world["poiFlags"]["Parents Room"]["Final"] = True
            world["poiFlags"]["Your Room"]["Final"] = True
            world["poiFlags"]["Kitchen"]["Final"] = True
            return world
        
'''
printParentsRoom:
Checks for certain flags and uses the userInput to give certain text and flags back to the world
It takes 2 parameters:
A world - see where everything is and where the player is at in the game, userInput - make choices based on users Input.
'''

#PARENTS ROOM PRINT
def printParentsRoom(world, userInput):
    import time
    #Detail text and leaving room
    if userInput.lower().strip() == "leave":
        if "slippers" not in world["player"]["inv"]:
            print(f"{printYOUColor(world)} need shoes that will make sure nobody hears a peep.")
            print(f"{printYOUColor(world)} shut the door as quietly as possible in hopes your parents don't hear the creaks of the door.\n")
        else:
            print(f"{printYOUColor(world)} shut the door as quietly as possible in hopes your parents don't hear the creaks of the door.\n")
        time.sleep(3)
        world["playerLoc"]["x"] = 5
        world["playerLoc"]["y"] = 3
        world["inMap"] = True
        return world
    #Detail text for dresser while checking if the game is in final state or if its not
    if userInput.lower().strip() == "dresser":
        if world["poiFlags"]["Parents Room"]["Final"] != True:
            print(f"\n{printYOUColor(world)} slowly open the drawer, trying not to make a sound...")
            time.sleep(2)
            print("Nothing but your mom's clothes. It smells of perfume\n")
            return world
        else:
            print(f"\n{printYOUColor(world)} slowly open the drawer, trying not to make a sound...")
            time.sleep(2)
            print("Nothing but your mom's clothes. It smells of perfume...")
            time.sleep(2)
            print(f"{printYOUColor(world)} rustle through the clothes, ignoring the overpowering smell.")
            time.sleep(3)
            print(f"{printYOUColor(world)} find a folded up piece of paper.")
            time.sleep(2)
            print(f"{printYOUColor(world)} unfold it and start reading...")
            time.sleep(3)
            print("It prints: '1st: RIGHT'\n")
            time.sleep(1)
            print(f"{printYOUColor(world)} wonder what it means.\n")
            return world
        #text for nightstand, checks if have key or not
    if userInput.lower().strip() == "nightstand":
        if "key" in world["player"]["inv"] or world["poiFlags"]["Parents Room"]["Final"] == True:
            print(f"\n{printYOUColor(world)} open the drawer as quietly as possible, your dad's snores growing louder...")
            time.sleep(3)
            print("Nothing but a pack of gum and iPhone charger now.\n")
        else:
            print(f"\n {printYOUColor(world)} open the drawer as quietly as possible, your dad's snores growing louder...")
            time.sleep(3)
            print("Rustling around finding various objects like a pack of gum, you spot something...")
            time.sleep(3)
            print(f"{printYOUColor(world)} pick up a shiny {KEY}... It may be useful.\n")
            time.sleep(2)
            world["player"]["inv"].append("key")
            world["stats"]["Items Collected"].append("key")
            return world
        #text for closet
    if userInput.lower().strip() == "closet":
        print(f"\n{printYOUColor(world)} open the closet door slowly, the door is creaky...")
        time.sleep(2)
        print("Nothing useful in here.\n")
        return world

'''
printYourRoom:
Checks for certain flags and uses the userInput to give certain text and flags back to the world
It takes 2 parameters:
A world - see where everything is and where the player is at in the game, userInput - make choices based on users Input.
'''
    
#YOUR ROOM PRINT
def printYourRoom(world, userInput):
    import time
    import random
    #Text for leaving
    if userInput.lower().strip() == "leave":
        print(f"\n{printYOUColor(world)} leave your room. Let's get out of here.\n")
        time.sleep(2)
        world["playerLoc"]["x"] = 3
        world["playerLoc"]["y"] = 5
        world["inMap"] = True
        return world
    #Sleep text dependent on random roll
    if userInput.lower().strip() == "sleep":
        randchoice = random.randint(0,1)
        if randchoice == 0:
            print(f"\n{printYOUColor(world)} lay in the bed and fall asleep...")
            time.sleep(2)
            print(f"{printYOUColor(world)} have a great dream but after a short while waken up by a loud BANG outside your room.")
            time.sleep(3)
            print(f"{printYOUColor(world)} need to get out of here.\n")
            time.sleep(3)
            return world
        else:
            print(f"\n{printYOUColor(world)} lay in the bed and fall asleep...")
            time.sleep(2)
            print("It only takes you 10 minutes to get waken up by a terrible nightmare.")
            time.sleep(3)
            print(f"{printYOUColor(world)} need to get out of here.\n")
            time.sleep(2)
            return world
    #Closet text dependent on if have slippers or not
    if userInput.lower().strip() == "closet":
        if "slippers" not in world["player"]["inv"]:
            print(f"\n{printYOUColor(world)} open the closet doors and see multiple jackets {printYOUColor(world)} always wear.")
            time.sleep(3)
            print(f"Your gaze shifts downward as {printYOUColor(world)} lay your eyes on your blue pair of {SLIPPERS}...")
            time.sleep(3)
            print("Perfect.\n")
            time.sleep(3)
            world["player"]["inv"].append("slippers")
            world["stats"]["Items Collected"].append("slippers")
            return world
        else:
            print(f"\n{printYOUColor(world)} open the closet doors and see multiple jackets {printYOUColor(world)} always wear.")
            time.sleep(3)
            print(f"{printYOUColor(world)} look for anything else that could be useful...")
            time.sleep(2)
            print("Nothing looks of use.\n")
            time.sleep(3)
    #look around text dependent on if in final phase or not
    if userInput.lower().strip() == "lookaround":
        if world["poiFlags"]["Your Room"]["Final"] == True:
            print(f"\n{printYOUColor(world)} look around your room examining harder than ever.")
            time.sleep(3)
            print(f"{printYOUColor(world)} spot tiny holes in the roof, even a cobweb in one of the corners")
            time.sleep(3)
            print(f"{printYOUColor(world)} turn your gaze towards the door and squint...")
            time.sleep(2)
            print(f"{printYOUColor(world)} see a folded piece of paper and grab it...")
            time.sleep(2)
            print(f"{printYOUColor(world)} unfold the piece of paper and it prints: '2nd: RIGHT'\n")
            time.sleep(4)
            return world
        else:
            print(f"{printYOUColor(world)} take a second to glance around the room")
            time.sleep(2)
            print("For the most part it is baron, but you notice some small details")
            time.sleep(2)
            print("A tiny rip in your jeans on the floor, even a cobweb in the corner of the room.")
            time.sleep(2)
            print("Gross.")
            time.sleep(2)
            return world

'''
printKitchen:
Checks for certain flags and uses the userInput to give certain text and flags back to the world
It takes 2 parameters:
A world - see where everything is and where the player is at in the game, userInput - make choices based on users Input.
'''

def printKitchen(world, userInput):
    import time
    #Leave text and functionality
    if userInput.lower().strip() == "leave":
        print(f"\n{printYOUColor(world)} walk out of the kitchen.\n")
        time.sleep(2)
        world["playerLoc"]["x"] = 1
        world["playerLoc"]["y"] = 3
        world["inMap"] = True
        return world
    #stove text and functionality
    if userInput.lower().strip() == "stove":
        if "steak" in world["player"]["inv"]:
            print(f"\n{printYOUColor(world)} walk towards the old stove with a {STEAK}.")
            time.sleep(3)
            print(f"{printYOUColor(world)} already have one, dont need another.")
            time.sleep(2)
            return world
        else:
            if world["Stove"] > 5:
                print(f"\n{printYOUColor(world)} walk towards the old stove with a {STEAK}.")
                time.sleep(3)
                print(f"{printYOUColor(world)} begin to cook the {STEAK}.")
                time.sleep(3)
                print("Looks edible.\n")
                time.sleep(2)
                world["player"]["inv"].append("steak")
                world["stats"]["Items Collected"].append("steak")
                world["Stove"] -=1
                return world
            if world["Stove"] == 1:
                print(f"\n{printYOUColor(world)} walk towards the old stove with a {STEAK}.")
                time.sleep(3)
                print(f"{printYOUColor(world)} begin to cook the {STEAK}.")
                time.sleep(3)
                print("Looks edible.\n")
                print(f"The stove looks disasterous. It will break down after cooking one more {STEAK}.\n")
                time.sleep(4)
                world["player"]["inv"].append("steak")
                world["stats"]["Items Collected"].append("steak")
                world["Stove"] -=1
                return world
            if world["Stove"] <= 3:
                print(f"\n{printYOUColor(world)} walk towards the old stove with a {STEAK}.")
                time.sleep(3)
                print(f"{printYOUColor(world)} begin to cook the {STEAK}.")
                time.sleep(3)
                print("Looks edible.\n")
                print("The stove looks really bad. It will break down soon.\n")
                time.sleep(4)
                world["player"]["inv"].append("steak")
                world["stats"]["Items Collected"].append("steak")
                world["Stove"] -=1
                return world
            if world["Stove"] <= 5:
                print(f"\n{printYOUColor(world)} walk towards the old stove with a {STEAK}.")
                time.sleep(3)
                print(f"{printYOUColor(world)} begin to cook the {STEAK}.")
                time.sleep(3)
                print("Looks edible.\n")
                print("The stove looks worse for wear.\n")
                time.sleep(4)
                world["player"]["inv"].append("steak")
                world["stats"]["Items Collected"].append("steak")
                world["Stove"] -=1
                return world
    #Eat text depending on state of hunger levels.
    if userInput.lower().strip() == "eat":
        if world["player"]["hunger"] == world["player"]["maxHung"]:
            print("\nCan't eat anymore. Already full.\n")
            time.sleep(2)
            return world
        world["player"]["hunger"] += 5
        if world["player"]["hunger"] >= world["player"]["maxHung"]:
            print(f"\n{printYOUColor(world)} ate the steak...")
            time.sleep(2)
            print("Very juicy, but kind of hard to get down...")
            time.sleep(3)
            print(f"{printYOUColor(world)} are now full!\n")
            time.sleep(2)
            world["player"]["hunger"] = world["player"]["maxHung"]
            world["player"]["inv"].remove("steak")
            return world
        if world["player"]["hunger"] < world["player"]["maxHung"]:
            print(f"\n{printYOUColor(world)} ate the {STEAK}...")
            time.sleep(2)
            print(f"{printYOUColor(world)} were so hungry, you wolfed down the {STEAK}, loving every bit of the taste...")
            time.sleep(3)
            print("Very Good!\n")
            time.sleep(2)
            world["player"]["inv"].remove("steak")
            return world
    #Text for fridge and checks if in final state or not.
    if userInput.lower().strip() == "fridge":
        if world["poiFlags"]["Kitchen"]["Final"] == True:
            print(f"\n{printYOUColor(world)} open the fridge as it cool air blasts in your face...")
            time.sleep(3)
            print("Those pickles look delicious.")
            time.sleep(1)
            print(f"{printYOUColor(world)} impulsively grab from them but when {printYOUColor(world)} do you feel something on the backside...")
            time.sleep(3)
            print(f"Turning them around, {printYOUColor(world)} find a folded piece of paper attached to the pickles!\n")
            time.sleep(2)
            print("Opening the piece of paper it prints: '3rd: LEFT'\n")
            time.sleep(4)
            return world
        else:
            print(f"\n{printYOUColor(world)} open the fridge as it cool air blasts in your face...")
            time.sleep(3)
            print(f"Looking around everything looks delicious to {printYOUColor(world)}.")
            time.sleep(2)
            print(f"{printYOUColor(world)} look longily at the pickles, the {STEAK} and the pizza rolls.")
            time.sleep(3)
            if world["player"]["hunger"] == world["player"]["maxHung"]:
                print("MMM.....\n")
                time.sleep(2)
                return world
            else:
                print(f"{printYOUColor(world)} feel hungry...\n")
                time.sleep(2)
                return world
    #Text for cabinet and checks if hungry or not
    if userInput.lower().strip() == "cabinet":
        print(f"\n{printYOUColor(world)} open the wooden cabinet and look around...")
        time.sleep(3)
        print("The chips, popcorn and granola bars look delicious...")
        time.sleep(2)
        if world["player"]["hunger"] == world["player"]["maxHung"]:
            print("MMM.....\n")
            time.sleep(2)
            return world
        else:
            print(f"{printYOUColor(world)} feel hungry...\n")
            time.sleep(2)
            return world
        
'''
printPostgame:
Checks for certain flags and uses the userInput to give certain text and flags back to the world
End Game loop
It takes 2 parameters:
A world - see where everything is and where the player is at in the game, userInput - make choices based on users Input.
'''

def printPostgame(world, userInput):
    #Checks for userInput
    import time
    if userInput.lower().strip() == "quit":
        #Ends game if quit is chosen
        print("\nThank you for playing!\n")
        time.sleep(3)
        exit()
    if userInput.lower().strip() == "stats":
        #Processes stats if stats is chosen 
        stats = readStats(world)
        print(stats)
        time.sleep(3)

            
        






            
    
    
            
        
    