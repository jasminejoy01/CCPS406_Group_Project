# -*- coding: utf-8 -*-
"""
Room#2: Storage for Construction Bots
"""
import Item as I
import utils
import OutdoorsMiddle
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
    T.ConstructionBotStorage.basicDes()
         
def fancyDes():
    T.ConstructionBotStorage.fancyDes()

def movewest():
    utils.x = utils.x + 1
    os.system('cls' if os.name == 'nt' else 'clear') 
    if not utils.advanced:
      OutdoorsMiddle.basicDes()
    else:
      OutdoorsMiddle.fancyDes()  


def movenorth():
    print("Woops! Can't go that way!")

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
    room.take(obj, itemdictionary, filename)

