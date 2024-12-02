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
                outputString += f"[{"X":>2}]"
            elif board[row][col] == 0:
                outputString += f"[{" ":2}]"
        outputString += "\n"
    print(outputString, end='')

