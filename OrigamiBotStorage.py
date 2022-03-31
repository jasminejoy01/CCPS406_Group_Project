# -*- coding: utf-8 -*-
"""
Room#3: Storage for Origami Bots.
"""

import Item as I
import utils

print("You're in the Origami Bot Storage.")

utils.roomsvisited[3] = 1

itemshere = []

def basicDes():
    print("There is a door to the West.")

def fancyDes():
    print("")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Outdoors (south)!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")
