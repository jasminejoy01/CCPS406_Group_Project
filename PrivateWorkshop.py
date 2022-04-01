# -*- coding: utf-8 -*-
"""
Room#1: Private Workshop
"""
import Item as I
import utils

#print("You're in the Private Workshop.")

utils.roomsvisited[0] = 1


itemshere = [I.computer1, I.nullItem]

def basicDes():
    print("A small room with a computer on a desk. There is a door to the West.")

def fancyDes():
    print("There room has no windows. There is a door to the left.")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Cleaning Bot Storage", utils.x, utils.y)


def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def moveeast():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def itemsInhere():
    print("A computer.")
    
def examine(obj):
    if obj == "computer":
        print("Got a computer.")
        I.Computer(False, "Password:").examine()
        I.Computer(False, "Password:").use()
    if obj == "stickynote":
        print("The notes mostly contain sketches of strange robots and bizarre contraptions, surrounded by hearts.")