# -*- coding: utf-8 -*-
"""
Room#9: The Exit
"""
import Item as I
import utils

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
    print("Congrats! You're exiting the Game!")

def moveeast():
    print("Woops! Can't go that way!")
