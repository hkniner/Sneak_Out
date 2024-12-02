from gameTools import *

'''
createBoard
creates a 2d array and returns it
It takes one parameter:
boardSize: representing the size of the board created
'''
def createBoard(boardSize):
    board = []
    for row in range(boardSize):
        board.append([])
        for col in range(boardSize):
            board[row].append(0)
    return board

'''
printBoard
puts board into outputString and displays it as a boardSize x boardSize board
It takes one parameter:
board: list that represents the board size
'''
def printBoard(world):
    outputString = "" #Empty String
    board = world["board"]
    for row in range(len(board)):

        for col in range(len(board)):
            if world["playerLoc"]["x"] == col and \
                world["playerLoc"]["y"] == row:
                #Print an X in the cell
                coloredX = setColor(world["player"]["color"], "X")
                outputString += f"[{coloredX :>2}]"
            elif world["POI"]["Front Door"]["x"] == col and \
                world["POI"]["Front Door"]["y"] == row:
                #Print an F in the cell
                coloredF = setColor("purple", "F")
                outputString += f"[{coloredF :>2}]"
            elif world["POI"]["Parents Room"]["x"] == col and \
                world["POI"]["Parents Room"]["y"] == row:
                #Print an P in the cell
                coloredP = setColor("purple", "P")
                outputString += f"[{coloredP :>2}]"
            elif world["POI"]["Your Room"]["x"] == col and \
                world["POI"]["Your Room"]["y"] == row:
                #Print an R in the cell
                coloredR = setColor("purple", "R")
                outputString += f"[{coloredR :>2}]"
            elif world["POI"]["Kitchen"]["x"] == col and \
                world["POI"]["Kitchen"]["y"] == row:
                #Print an K in the cell
                coloredK = setColor("purple", "K")
                outputString += f"[{coloredK :>2}]"
            elif board[row][col] == 0:
                outputString += f"[{" ":2}]"
        outputString += "\n"
    print(outputString, end='')

