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

printBoard(world)