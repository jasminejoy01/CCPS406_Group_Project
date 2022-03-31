# -*- coding: utf-8 -*-
"""
Room#4: Outdoors North
"""
import Item as I
import utils

print("You've stepped outside into the North corridoors.")

utils.roomsvisited[4] = 1

itemshere = []

def basicDes():
    print("Outside space between the storage building and main lab")

def fancyDes():
    print("The open paved area continues South. There is a grassy area with picnic benches to the the West.")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y + 0
    #print(utils.x, utils.y)
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("Now, you're moving to Greenspace break area!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    utils.x = utils.x + 0
    utils.y = utils.y + 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Outdoors (middle)!", utils.x, utils.y)

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Cleaning Bot Storage!", utils.x, utils.y)
