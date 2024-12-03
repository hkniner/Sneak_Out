'''
COS 121 Final: Sneak Out!
Game by: Henry Koch
Dec 2, 2024
'''
#importing all other python files
from boardTools import *
from gameTools import *
from inputProcess import *
from poiProcess import *
import time

def main():
    # Creating world and location of player
    world = {}
    loc = {
        "x":3,
        "y":3
    }
    world["board"] = createBoard(7)
    world["playerLoc"] = loc
    world["player"] = createPlayer()
    world["inMap"] = True

    #creating pois and locations
    world["POI"] = {}
    world["POI"]["Front Door"] = {
        "x":3,
        "y":0
    }
    world["POI"]["Parents Room"] = {
        "x":6,
        "y":3
    }
    world["POI"]["Your Room"] = {
        "x":3,
        "y":6
    }
    world["POI"]["Kitchen"] = {
        "x":0,
        "y":3
    }
    #Creating all POI flags, basically telling what to do and when 
    world["poiFlags"] = {}
    world["poiFlags"]["Front Door"] = {
        "Key": True,
        "Unlock": False,
        "Finish": False,
        "InKeyGame": False
    }
    world["poiFlags"]["Parents Room"] = {
        "Slippers": False,
        "Key": False,
        "Final": False,
    }
    world["poiFlags"]["Your Room"] = {
        "Slippers": False,
        "Final": False
    }
    world["poiFlags"]["Kitchen"] = {
        "Stove": False,
        "Final": False,
    }
        
    #Intro Cutscene

    print(f"As the night's got warmer and the day's became longer {world["player"]["name"]} was lying in their bed...")
    time.sleep(4)
    print("With a growing urge that could not be ignored any longer...")
    time.sleep(4)
    print("The urge to...")
    time.sleep(2)
    print("SNEAK OUT!!!!")
    time.sleep(2)


    #Gameplay loop
    while True:
        #Checks to see if game is done
        if world["poiFlags"]["Front Door"]["Finish"] == True:
            break
        #Checks to see if in minimap
        if world["inMap"] == True:
            #Prints map
            printBoard(world)
            printHunger(world)
            #Asks user for command
            userInput = getUserComm(world)
            #Processes userInput
            world["player"]["hunger"] -= 1
            processUserComm(world, loc, userInput)
        if world["inMap"] == False:
            #Checks which POI player located at and prints dependent on that POI
            if world["playerLoc"] == world["POI"]["Front Door"]:
                userInput = getUserComm(world)
                printFrontDoor(world, userInput)
            if world["playerLoc"] == world["POI"]["Parents Room"]:
                print("parents room")
                break
            if world["playerLoc"] == world["POI"]["Your Room"]:
                print("your room")
                break
            if world["playerLoc"] == world["POI"]["Kitchen"]:
                print("kitchen")
                break

main()