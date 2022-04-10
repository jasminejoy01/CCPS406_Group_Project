# -*- coding: utf-8 -*-
"""
Room#17: Hallway 1
"""
import Item as I
import utils
import PrototypeWorkshop
import BotTesting
import BuildingEntranceExit
import Hallway2
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
    T.Hallway1.basicDes()
         
def fancyDes():
    T.Hallway1.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
        PrototypeWorkshop.basicDes()
    else:
        PrototypeWorkshop.fancyDes()

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    if not utils.advanced:
        BotTesting.basicDes()
    else:
        BotTesting.fancyDes()  

def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        Hallway2.basicDes()
    else:
        Hallway2.fancyDes()
 
def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
        BuildingEntranceExit.basicDes()
    else:
        BuildingEntranceExit.fancyDes()

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
