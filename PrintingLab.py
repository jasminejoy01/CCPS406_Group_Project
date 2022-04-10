# -*- coding: utf-8 -*-
"""
Room#24: 3D Printing Lab
"""
import Item as I
import utils
import Hallway2
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
  'terminal':  [terminal1     , None ]    
}

def basicDes():
    T.PrintingLab.basicDes()
         
def fancyDes():
    T.PrintingLab.fancyDes()
    
def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    utils.roomsvisited[18] = 1
    if not utils.advanced:
        Hallway2.basicDes()
    else:
        Hallway2.fancyDes()

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary)
