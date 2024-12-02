'''
COS 121 Final: Sneak Out!
Game by: Henry Koch
Dec 2, 2024
'''
#importing all other python files
from boardTools import *
from gameTools import *
from inputProcess import *

# Creating world and location of player
world = {}
loc = {
    "x":3,
    "y":3
}
world["board"] = createBoard(7)
world["playerLoc"] = loc
world["player"] = createPlayer()

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
printBoard(world)