# -*- coding: utf-8 -*-
"""
Room#6: Outside space between the storage building and main lab
"""
import Item as I
import utils

print("You've stepped into the South corridoors outside.")

utils.roomsvisited[6] = 1

itemshere = []

def basicDes():
    print("The paved outdoor area continues to the North.")

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
    #print("You're moving back to Outdoors (middle)!", utils.x, utils.y)

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Origami Bot Storage!", utils.x, utils.y)
