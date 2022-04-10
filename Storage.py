# -*- coding: utf-8 -*-
"""
Room#7: Storage room
"""
import Item as I
import utils
import Item2 as I2
import Hallway6
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
 
}

def basicDes():
    T.Storage.basicDes()
    I2.Lost_Found.item_add()
    I2.StorageCloset.disguise()
         
def fancyDes():
    T.Storage.fancyDes()
    I2.Lost_Found.item_add()
    I2.StorageCloset.disguise()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        Hallway6.basicDes()
    else:
        Hallway6.fancyDes()
  
def moveeast():
    print("Woops! Can't go that way!")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
