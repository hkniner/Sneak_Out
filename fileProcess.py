from gameTools import *

'''
writeStats:
writes the string put into the file into a file called stats.txt
It takes one parameter:
statsString - has to be a string
'''

def writeStats(world):
    dashct = 21 - ((len(world["player"]["name"]) - 11) + 5)
    dashstr = dashct * "-"
    f = open("data.csv", "a")
    f.write(f"{world["stats"]["docStr"]},{world["player"]["txtName"]},{world["stats"]["Time Played"]},\
{world["stats"]["Cycle Count"]},{world["stats"]["Hunger Used"]},{world["stats"]["Items Collected"]}")
    f.write("\n")
    f.close()

def processStats(world):
    outputString = ""
    try:
        f = open("data.csv", "r")
        contents = f.read().split("\n")
        for i in range(len(contents)):
            print(i)
            if f"Character created on: {world["stats"]["docStr"]}" == i:
                print(i)
                outputString += i - 1
                outputString += i
                outputString += i + 1
                outputString += i + 2
                outputString += i + 3
                outputString += i + 4
                outputString += i + 5
                outputString += i + 6
        return outputString
    except FileNotFoundError:
        print("File not found.")
        print("Creating 'stats.txt'")
        f = open("stats.txt", "a")
        f.close()



