'''
COS 121 Final: Sneak Out!
Game by: Henry Koch
Dec 2, 2024
'''
#importing all other python files
from boardTools import *
from gameTools import *
from inputProcess import *
from gameProcess import *
from fileProcess import *
from datetime import datetime
import time


def main():
    # Creating csv.data file
    try:
        f = open("data.csv", "r")
        f.close()
    except:
        f = open("data.csv", "w")
        f.write("open,date,name,played,cycles,hunger,items,close")
        f.write("\n")
        f.close()
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
    world["maxStove"] = sum(dndDiceRoll("6d2"))
    world["Stove"] = world["maxStove"]
    world["GameWon"] = True
    world["GameOver"] = False
    world["PostGame"] = False

    #Creating Stats
    world["stats"] = {}
    creation_date = datetime.now()
    world["stats"]["docStr"] = creation_date
    creation_date = f"Character created on: {creation_date}"
    world["stats"]["Date of Creation"] = creation_date
    world["stats"]["start time"] = time.time()
    world["stats"]["Cycle Count"] = 0
    world["stats"]["Hunger Used"] = 0
    world["stats"]["Items Collected"] = []

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
        "Unlock": False,
        "Finish": True,
        "InKeyGame": False
    }
    world["poiFlags"]["Parents Room"] = {
        "Final": False,
    }
    world["poiFlags"]["Your Room"] = {
        "Final": False
    }
    world["poiFlags"]["Kitchen"] = {
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
        world["stats"]["Cycle Count"] += 1
        #Checks to see if game is done
        if world["poiFlags"]["Front Door"]["Finish"] == True:
            world["GameWon"] = True
            break
        if world["GameOver"] == True:
            break
        #Checks to see if in minimap
        if world["inMap"] == True:
            #Prints map
            printBoard(world)
            printHunger(world)
            #Asks user for command
            userInput = getUserComm(world)
            #Processes userInput
            processUserComm(world, loc, userInput)
        if world["inMap"] == False:
            #Checks which POI player located at and prints dependent on that POI
            if world["playerLoc"] == world["POI"]["Front Door"]:
                userInput = getUserComm(world)
                printFrontDoor(world, userInput)
            if world["playerLoc"] == world["POI"]["Parents Room"]:
                userInput = getUserComm(world)
                printParentsRoom(world, userInput)
            if world["playerLoc"] == world["POI"]["Your Room"]:
                userInput = getUserComm(world)
                printYourRoom(world, userInput)
            if world["playerLoc"] == world["POI"]["Kitchen"]:
                userInput = getUserComm(world)
                printKitchen(world, userInput)
    #Finishing up statistics then processing
    world["stats"]["end time"] = time.time()
    world["stats"]["Time Played"] = world["stats"]["end time"] - world["stats"]["start time"]
    txtStatString = processTxtStats(world)

        
    if world["GameOver"] == True:
        print(f"\n{world["player"]["name"]} fell to the ground as his conciousness left...\n")
        print(f"\nGAME OVER!!!\n")
    else:
        world["PostGame"] = True
        writeStats(world)
        while True:
            userInput = getUserComm(world)
            printPostgame(world, userInput)



main()