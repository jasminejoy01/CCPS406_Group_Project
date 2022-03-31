# -*- coding: utf-8 -*-
"""
Room#15: Security Office
"""

import Item as I
import utils

print("You're in the Security Office.")

utils.roomsvisited[15] = 1

itemshere = []

def basicDes():
    print("Here is a door to the North.")

def fancyDes():
    print("")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    utils.x = utils.x - 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Hallway - Section 5.")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")
