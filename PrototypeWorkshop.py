# -*- coding: utf-8 -*-
"""
Room#23: The Prototyping Lab"
"""
import Item as I
import utils

print("You're in the Prototyping Lab.")

utils.roomsvisited[23] = 1

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
    #print("You're moving back into Hallway #1.")
