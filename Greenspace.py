# -*- coding: utf-8 -*-
"""
Room#10: Greenspace break area
"""
import Item as I
import utils

print("You're in the Greenspace area.")

utils.roomsvisited[10] = 1

itemshere = []

def basicDes():
    print("An outdoor greenspace.")

def fancyDes():
    print("There is an open paved area to the East.")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Outdoors (North)!", utils.x, utils.y)
