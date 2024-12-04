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

                    print(count)
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
                        print("all set")
                        count += 1
                        continue
                    if i == 2 and userInput == correct_combo[i]:
                        print("all set")
                        count += 1
                        continue
                    if i == 3 and userInput == correct_combo[i]:
                        print("all set")
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
    
    
            
        
    