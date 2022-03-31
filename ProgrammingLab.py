# -*- coding: utf-8 -*-
"""
Room#12: Programming Lab"
"""
import Item as I
import utils

print("You're in the Programming Lab.")

utils.roomsvisited[12] = 1

itemshere = []

def basicDes():
    print("here is a door to the West.")

def fancyDes():
    print("")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back into Hallway #2.")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")
