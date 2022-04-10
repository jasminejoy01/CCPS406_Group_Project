# -*- coding: utf-8 -*-
"""
Room#8: Hallway 6
"""
import Item as I
import utils
import Storage
import Exit
import Hallway5
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
}

def basicDes():
    T.Hallway6.basicDes()
         
def fancyDes():
    T.Hallway6.fancyDes()

def movewest():  
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
        Hallway5.basicDes()
    else:
        Hallway5.fancyDes()

def movenorth(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    if not utils.advanced:
        Storage.basicDes()
    else:
        Storage.fancyDes()


def movesouth():
  if utils.EMgate:
    print("I shouldn't try to leave yet. The electromagnetic security gate is still up. I'd be fried!")
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        Exit.basicDes()
    else:
        Exit.fancyDes()

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
