from gameTools import *

'''
writeStats:
writes the string put into the file into a file called stats.txt
It takes one parameter:
statsString - has to be a string
'''

def writeStats(world):
    f = open("data.csv", "a")
    f.write(f"{world["stats"]["docStr"]},{world["player"]["txtName"]},{world["stats"]["Time Played"]},\
{world["stats"]["Cycle Count"]},{world["stats"]["Hunger Used"]},{world["stats"]["Items Collected"]}")
    f.write("\n")
    f.close()
    f = open("stats.txt", "a")
    f.write(processTxtStats(world))
    f.close()

def readStats(world):
    f = open("data.csv", "r")
    contents = f.read().split("\n")
    contents.pop(0)
    while "" in contents:
        contents.remove("")
    for i in contents:
        i = i.split(',')
        if i[0] == str(world["stats"]["docStr"]):
            stats = processStats(world)
            return stats



