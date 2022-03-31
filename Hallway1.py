# -*- coding: utf-8 -*-
"""
Room#17: Hallway 1
"""
import Item as I
import utils

print("You're in the Hallway#1.")

utils.roomsvisited[17] = 1

itemshere = []

def basicDes():
    print("The hall continues south. The security desk is East, and there are doors North and West.")

def fancyDes():
    print("")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Prototype Shop!")

def movenorth():
    utils.x = utils.x
    utils.y = utils.y - 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Bot Testing Simple Tasks")

def movesouth():
    utils.x = utils.x
    utils.y = utils.y + 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're  moving into Hallway 2!")

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back into Building Entrance/Exit.")
