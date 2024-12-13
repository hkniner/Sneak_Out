from gameTools import *

'''
createBoard
creates a 2d array and returns it
It takes one parameter:
boardSize: representing the size of the board created
'''
def createBoard(boardSize):
    #Creates board
    board = []
    #Fills list wth different lists and 0 in all boxes
    for row in range(boardSize):
        board.append([])
        for col in range(boardSize):
            board[row].append(0)
    return board

'''
printBoard
puts board into outputString and displays it as a boardSize x boardSize board
It takes one parameter:
world: dictionary that contains the board list
'''
def printBoard(world):
    outputString = "" #Empty String
    board = world["board"]
    #Creating and printing UI
    dashct = 21 - ((len(world["player"]["name"]) - 11) + 5)
    dashstr = dashct * "-"
    print(f"---------{world["player"]["name"]}'s HOUSE" + f"{dashstr}")

#Visualizing board with blank spots or POIs then filling into outputString
    for row in range(len(board)):

        for col in range(len(board)):
            #Printing player
            if world["playerLoc"]["x"] == col and \
                world["playerLoc"]["y"] == row:
                #Print an X in the cell
                coloredX = setColor(world["player"]["color"], "X")
                outputString += f"[{coloredX:>2}"
                outputString += f"{" ":>1}]"
            
            #Printing Front Door POI
            elif world["POI"]["Front Door"]["x"] == col and \
                world["POI"]["Front Door"]["y"] == row:
                #Print an F in the cell
                coloredF = setColor("purple", "F")
                outputString += f"[{coloredF:>2}"
                outputString += f"{" ":>1}]"
            
            #Printing Parents Room POI
            elif world["POI"]["Parents Room"]["x"] == col and \
                world["POI"]["Parents Room"]["y"] == row:
                #Print an P in the cell
                coloredP = setColor("purple", "P")
                outputString += f"[{coloredP:>2}"
                outputString += f"{" ":>1}]"
            
            #Printing Your Room POI
            elif world["POI"]["Your Room"]["x"] == col and \
                world["POI"]["Your Room"]["y"] == row:
                #Print an R in the cell
                coloredR = setColor("purple", "R")
                outputString += f"[{coloredR:>2}"
                outputString += f"{" ":>1}]"
            
            #Printing Kitchen POI
            elif world["POI"]["Kitchen"]["x"] == col and \
                world["POI"]["Kitchen"]["y"] == row:
                #Print an K in the cell
                coloredK = setColor("purple", "K")
                outputString += f"[{coloredK:>2}"
                outputString += f"{" ":>1}]"

            #Printing Empty Spaces
            elif board[row][col] == 0:
                outputString += f"[{" ":2}]"
        outputString += "\n"
    print(outputString, end='')
    print(f"---------------------------------")