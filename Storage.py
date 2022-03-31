# -*- coding: utf-8 -*-
"""
Room#7: Storage room
"""

import Item as I
import utils

print("You're in the Storage Room.")

utils.roomsvisited[7] = 1

itemshere = []

def basicDes():
    print("There's a lost and found box full of odd hats and coats. There is a door to the South.")

def fancyDes():
    print("")

def movewest():
    print("Woops! Can't go that way!")


def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    utils.x = utils.x + 0
    utils.y = utils.y + 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway - Section 6!")

def moveeast():
    print("Woops! Can't go that way!")
