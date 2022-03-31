# -*- coding: utf-8 -*-
"""
Room#21: Head of Origami Office.
"""

import Item as I
import utils

print("You're in the Head of Origami Office.")

utils.roomsvisited[21] = 1

itemshere = []

def basicDes():
    print("There is a door to the West.")

def fancyDes():
    print("")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    utils.x = utils.x
    utils.y = utils.y - 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway#4.")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")
