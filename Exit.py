# -*- coding: utf-8 -*-
"""
Room#9: The Exit
"""
import Item as I
import utils
import os

print("The ultimate goal.")

utils.roomsvisited[9] = 1

itemshere = []

def basicDes():
    print("The hall continues West. There are doors North and South.")

def fancyDes():
    print("")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    utils.x = utils.x + 0
    utils.y = utils.y - 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway6!")

def movesouth():
    if utils.GPS == False and utils.disguise == True:
        print("Congrats! You're exiting the Game!")
        os.remove('save.py')
    elif utils.GPS == True and utils.disguise == True:
        print("Your disguise is great, but they can still find you because your GPS tracker is on.\n You need to find your Creator to turn off your GPS tracker.")
    elif utils.GPS == False and utils.disguise == False:
        print("Your GPS is off, but you still need a disguise to leave the building.\n Go back in the Storage Closet and find a disguise so that you won't be spotted when you leave.")
    else:
        print("Congrats! You're exiting the Game!")

def moveeast():
    print("Woops! Can't go that way!")
