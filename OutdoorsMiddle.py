# -*- coding: utf-8 -*-
"""
Room#5: Outside space between the storage building and main lab
"""
import Item as I
import utils

print("You've stepped into the Middle corridoors outside.")

utils.roomsvisited[5] = 1

itemshere = []

def basicDes():
    print("The paved outdoor area continues North and South. There are doors to the East and West.")

def fancyDes():
    print("")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("Now, you're moving to Greenspace break area!", utils.x, utils.y)

def movenorth():
    utils.x = utils.x
    utils.y = utils.y - 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Outdoors (north)!", utils.x, utils.y)

def movesouth():
    utils.x = utils.x
    utils.y = utils.y + 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Outdoors (middle)!", utils.x, utils.y)

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Construction Bot Storage!", utils.x, utils.y)
