# -*- coding: utf-8 -*-
"""
Room#10: Greenspace break area
"""
import Item as I
import utils
import OutdoorsNorth
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText

itemdictionary = { # [Item, isLocked]
}

def basicDes():
    T.Greenspace.basicDes()

def fancyDes():
    T.Greenspace.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
        OutdoorsNorth.basicDes()
    else:
        OutdoorsNorth.fancyDes()
   
def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
