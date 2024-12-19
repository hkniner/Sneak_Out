COS 121 Final: Sneak Out!
Game created by: Henry Koch
Started on Dec 2, 2024

FILE TO PLAY : main.py

Sneak Out is a text-adventure based game that works off userInput processing and updating
using a game loop. Starting it initalizes the game by creating the world and player. Then the 
player is dropped into a board like mini map where they can traverse using hunger(cycles). If 
your hunger drops to 0, game over. There are many different rooms in the minimap(or house) you 
can traverse through and each plays an important role to finishing the actual game or finally 
sneaking out of the house. Once the game is over and you have sucessfully completed it, a save
file is written in both TXT and CSV format, if the 'stats' command is called, takes the csv data
and displays it in a user friendly way back on the screen. If you want to see stats of all players
made visit, 'stats.txt'. A early version of a draw-up of 'Sneak Out!' is avaiable in 'SneakOutChart.JPG'

Thank you for playing!

*FOR PROFESSOR SCHOTTER*

Sneak Out starts by spawning you in the middle of the minimap
-The first step in completing the game is by going down to your room.
-Looking in the closet will allow you to get the slippers(which are needed to get into the parents room)
-Sleeping will randomly give you flavor text for a good dream or bad one
-Looking around does nothing but give flavor text

After leaving your room, it is advised to go to the kitchen so you dont run out of hunger
-Stove lets you cook a steak and adds it into your inventory and allows you to eat it
  -The stove spawns in with a set amount of uses, adding flavor text for when it starts to break down, Then
  removes the option once it has been used up.
  -Each steak recovers 5 hunger.
-Fridge has flavor text
-Cabinets have flavor text

Next, going to the parents room is the next part, and since you have the slippers, you dont get kicked out
once you enter
-Going to the nightstand you find a key to the front door, which is used to sneak out
-Closet has flavor text
-Dresser has flavor text

Now, going to the front door and its finally time to sneak out
-Sneakout initalizes the final phase, in which the door now needs specific key turns to fully unlock the door
-While the game is in this "final phase" some flavor text in the rooms has changed:
    -In the "Parents room", you now find the note: "1st RIGHT" in the dresser
    -In "your room", you now find the note: "2nd RIGHT" while looking around
    -In "the kitchen", you now find the note: "3rd LEFT", while looking in the Fridge
-These act as the final key for finishing the game as when you go back to the sneakout option at the front door
-Now at the sneakout option you will be presented with the "key game", asking you to turn the key left or right
    -The game tells you if your right or wrong at the end of the 3 turns, so it is much harder to bruteforce, even
    though it is possible
    -Using the hints the final combination is discovered "right, right, left" the door will be unlocked,
    final cutscene plays while player stats are saved and written to the 2 files 

Finally, after the game is complete you are taken to the postgame screen
-You can choose stats, to get a user friendly view of the stats for the player you just completed the game with
-Or you can choose quit, which ends the program entirely.


