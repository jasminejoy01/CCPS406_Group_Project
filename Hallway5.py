# -*- coding: utf-8 -*-
"""
Room#14: Hallway 5
"""
import Item as I
import utils

print("You're in the Hallway#5.")

utils.roomsvisited[14] = 1

itemshere = []

def basicDes():
    print("The hall continues East and West. There is a door to the South.")

def fancyDes():
    print("")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway#4!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    utils.x = utils.x
    utils.y = utils.y + 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Security Room.")

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into into Hallway#6!")
