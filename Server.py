# -*- coding: utf-8 -*-
"""
Room#26: Server room
"""
import Item as I
import utils

print("You're in the Server room.")

utils.roomsvisited[26] = 1

itemshere = []

def basicDes():
    print("There is a door to the East.")

def fancyDes():
    print("")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway#4.")
