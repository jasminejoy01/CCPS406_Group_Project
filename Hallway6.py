# -*- coding: utf-8 -*-
"""
Room#8: Hallway 6
"""
import Item as I
import utils

print("You're in the Hallway#6.")

utils.roomsvisited[8] = 1

itemshere = []

def basicDes():
    print("The hall continues West. There are doors North and South.")

def fancyDes():
    print("")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway Section 5!")

def movenorth():
    utils.x = utils.x + 0
    utils.y = utils.y - 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into the lost and found storage room!")

def movesouth():
    utils.x = utils.x + 0
    utils.y = utils.y + 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're exiting the Building!")

def moveeast():
    print("Woops! Can't go that way!")
