# -*- coding: utf-8 -*-
"""
Room#20: Hallway 4
"""
import Item as I
import utils

print("You're in the Hallway#4.")

utils.roomsvisited[20] = 1

itemshere = []

def basicDes():
    print("The hall continues North and East. There are doors South and West.")

def fancyDes():
    print("")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Server Room!")

def movenorth():
    utils.x = utils.x
    utils.y = utils.y - 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway#3.")

def movesouth():
    utils.x = utils.x
    utils.y = utils.y + 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're  moving into Hallway#5.")

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Origami Head’s Office.")
