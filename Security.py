# -*- coding: utf-8 -*-
"""
Room#15: Security Office
"""

import Item as I
import utils
import Hallway5
import time
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, islocked, canTake, inInventory, description, interactable, useText, unlockText
#nullItem = I.Item("", False, False, False, "", False, "", "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}

def basicDes():
    T.Security.basicDes()
         
def fancyDes():
    T.Security.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():  
    if not utils.advanced:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[14] == 1:
            utils.y = utils.y + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            utils.roomsvisited[14] = 1
            Hallway5.basicDes()
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[14] == 1:
            utils.y = utils.y + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway5.fancyDes()
            utils.roomsvisited[14] = 1
        else:
            print("The door is locked.")   

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary)
