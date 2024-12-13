from gameTools import *

'''
writeStats:
writes the string put into the file into a file called data.csv and stats.txt as user interpretable.
It takes one parameter:
statsString - has to be a string
'''

def writeStats(world):
    #opens data file
    f = open("data.csv", "a")
    #adds data then makes a new line
    f.write(f"{world["stats"]["docStr"]},{world["player"]["txtName"]},{world["stats"]["Time Played"]},\
{world["stats"]["Cycle Count"]},{world["stats"]["Hunger Used"]},{world["stats"]["Items Collected"]}")
    f.write("\n")
    f.close()
    #writes stats to stats.txt in user interpretable format.
    f = open("stats.txt", "a")
    f.write(processTxtStats(world))
    f.close()

'''
readStats:
reads data.csv and cleans it up then proceeds to look for the data of creation of the particular instance 
to process it and return it
It has one parameter:
world - to read the date of creation and write stats
'''
def readStats(world):
    #Opens data file to read then splits entries and removes legend
    f = open("data.csv", "r")
    contents = f.read().split("\n")
    contents.pop(0)
    #removes blank entrys
    while "" in contents:
        contents.remove("")
    #splits entries into individual datapieces
    for i in contents:
        i = i.split(',')
        #checks for current date of creation(doc)
        if i[0] == str(world["stats"]["docStr"]):
            stats = processStats(world)
            return stats



