from inputProcess import *

#FRONT DOOR PRINT
def printFrontDoor(world, userInput):
    import time
    #Detail text and leaving room
    if userInput.lower().strip() == "leave":
        print("You leave the daunting door as your want for freedom grows.\n")
        world["playerLoc"]["x"] = 3
        world["playerLoc"]["y"] = 1
        world["inMap"] = True
        return world
    #One option on what to do here: sneakout
    if userInput.lower().strip() == "sneakout":
        #Checks to see if have key and want to sneakout

        if world["poiFlags"]["Front Door"]["Unlock"] == True:
            print("\nAs you approached the door and grabbed on the doorknob, you paused waiting for your freedom...")
            time.sleep(4)
            print("You jostled the door...")
            time.sleep(3)
            print("You try to open it...\n")

            #Key Game
            
            while True:
                world["poiFlags"]["Front Door"]["InKeyGame"] = True
                count = 0
                for i in range(1,5):

                    #Check if done then returns result

                    if i == 4:
                        if count == 3:
                            print("\nThe Door is now Unlocked!")
                            world["poiFlags"]["Front Door"]["Finish"] = True
                            world["poiFlags"]["Front Door"]["InKeyGame"] = False
                            return world
                        else:
                            print("\nYou jostled the door knob more and more but...")
                            print("Its still locked.\n")
                            world["poiFlags"]["Front Door"]["InKeyGame"] = False
                            return world
                    correct_combo = ["ph", "right", "right", "left"]
                    userInput = getUserComm(world)

                    #Checks to see if individual response correct then adds something to list
                    if userInput == "leave":
                        print("\nYou jostled the door knob more and more but...")
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

        if world["poiFlags"]["Front Door"]["Key"] == False:
            print("\nAs you approached the door and grabbed on the doorknob, you paused waiting for your freedom...")
            time.sleep(4)
            print("You jostled the door...")
            time.sleep(3)
            print("It's locked.\n")
            return world
        if world["poiFlags"]["Front Door"]["Key"] == True:
            print("\nAs you approached the door and grabbed on the doorknob, you paused waiting for your freedom...")
            time.sleep(4)
            print("You jostled the door...")
            time.sleep(3)
            print("It's not locked, but as another failsafe, your annoying parents made a combination, there's a certain combination to turn the key.")
            print("(Return to this area to try a combination.)\n")
            world["player"]["inv"].remove("key")
            world["poiFlags"]["Front Door"]["Unlock"] = True
            return world

#PARENTS ROOM PRINT
def printParentsRoom(world, userInput):
    import time
    #Detail text and leaving room
    if userInput.lower().strip() == "leave":
        if "slippers" not in world["player"]["inv"]:
            print("You need shoes that will make sure nobody hears a peep.")
            print("You shut the door as quietly as possible in hopes your parents don't hear the creaks of the door.\n")
        else:
            print("You shut the door as quietly as possible in hopes your parents don't hear the creaks of the door.\n")
        time.sleep(3)
        world["playerLoc"]["x"] = 5
        world["playerLoc"]["y"] = 3
        world["inMap"] = True
        return world
    #Detail text for dresser while checking if the game is in final state or if its not
    if userInput.lower().strip() == "dresser":
        if world["poiFlags"]["Parents Room"]["Final"] != True:
            print("\nYou slowly open the drawer, trying not to make a sound...")
            time.sleep(2)
            print("Nothing but your mom's clothes. It smells of perfume\n")
            return world
        else:
            print("\nYou slowly open the drawer, trying not to make a sound...")
            time.sleep(2)
            print("Nothing but your mom's clothes. It smells of perfume...")
            time.sleep(2)
            print("You rustle through the clothes, ignoring the overpowering smell.")
            time.sleep(3)
            print("You find a folded up piece of paper.")
            time.sleep(2)
            print("You unfold it and start reading...")
            time.sleep(3)
            print("It prints: '1st: RIGHT'\n")
            time.sleep(1)
            print("You wonder what it means.\n")
            return world
        #text for nightstand, checks if have key or not
    if userInput.lower().strip() == "nightstand":
        if "key" in world["player"]["inv"] or world["poiFlags"]["Parents Room"]["Final"] == True:
            print("\nYou open the drawer as quietly as possible, your dad's snores growing louder...")
            time.sleep(3)
            print("Nothing but a pack of gum and iPhone charger now.\n")
        else:
            print("\n You open the drawer as quietly as possible, your dad's snores growing louder...")
            time.sleep(3)
            print("Rustling around finding various objects like a pack of gum, you spot something...")
            time.sleep(3)
            print("You pick up a shiny key... It may be useful.\n")
            time.sleep(2)
            world["player"]["inv"].append("key")
            return world
        #text for closet
    if userInput.lower().strip() == "closet":
        print("\nYou open the closet door slowly, the door is creaky...")
        time.sleep(2)
        print("Nothing useful in here.\n")
        return world
    
#YOUR ROOM PRINT
def printYourRoom(world, userInput):
    import time
    import random
    #Text for leaving
    if userInput.lower().strip() == "leave":
        print("\nYou leave your room. Let's get out of here.\n")
        time.sleep(2)
        world["playerLoc"]["x"] = 3
        world["playerLoc"]["y"] = 5
        world["inMap"] = True
        return world
    if userInput.lower().strip() == "sleep":
        randchoice = random.randint(0,1)
        if randchoice == 0:
            print("\nYou lay in the bed and fall asleep...")
            time.sleep(2)
            print("You have a great dream but after a short while waken up by a loud BANG outside your room.")
            time.sleep(3)
            print("You need to get out of here.\n")
            time.sleep(3)
            return world
        else:
            print("\nYou lay in the bed and fall asleep...")
            time.sleep(2)
            print("It only takes you 10 minutes to get waken up by a terrible nightmare.")
            time.sleep(3)
            print("You need to get out of here.\n")
            time.sleep(2)
            return world
    if userInput.lower().strip() == "closet":
        if "slippers" not in world["player"]["inv"]:
            print("\nYou open the closet doors and see multiple jackets you always wear.")
            time.sleep(3)
            print("Your gaze shifts downward as you lay your eyes on your blue pair of slippers...")
            time.sleep(3)
            print("Perfect.\n")
            time.sleep(3)
            world["player"]["inv"].append("slippers")
            return world
        else:
            print("\nYou open the closet doors and see multiple jackets you always wear.")
            time.sleep(3)
            print("You look for anything else that could be useful...")
            time.sleep(2)
            print("Nothing looks of use.\n")
            time.sleep(3)
    if userInput.lower().strip() == "lookaround":
        if world["poiFlags"]["Your Room"]["Final"] == True:
            print("\nYou look around your room examining harder than ever.")
            time.sleep(3)
            print("You spot tiny holes in the roof, even a cobweb in one of the corners")
            time.sleep(3)
            print("You turn your gaze towards the door and squint...")
            time.sleep(2)
            print("You see a folded piece of paper and grab it...")
            time.sleep(2)
            print("You unfold the piece of paper and it prints: '2nd: RIGHT'\n")
            time.sleep(4)
            return world
        else:
            print("You take a second to glance around the room")
            time.sleep(2)
            print("For the most part it is baron, but you notice some  small details")
            time.sleep(2)
            print("A tiny rip in your jeans on the floor, even a cobweb in the corner of the room.")
            time.sleep(2)
            print("Gross.")
            time.sleep(2)
            return world


            
    
    
            
        
    