# -*- coding: utf-8 -*-
"""
Room#4: Outdoors North
"""
import Item as I
import utils
import Greenspace
import OutdoorsMiddle
import CleaningBotStorage
import text as T
import os
import room
import Terminal as term

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
terminal1 = term.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}
terminal1.locked = False

def basicDes():
    T.OutdoorNorth.basicDes()
          
def fancyDes():
    T.OutdoorNorth.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
        Greenspace.basicDes()
    else:
        Greenspace.fancyDes()
  
def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        OutdoorsMiddle.basicDes()
    else:
        OutdoorsMiddle.fancyDes()
   
def moveeast():    
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
      CleaningBotStorage.basicDes()
    else:
      CleaningBotStorage.fancyDes()

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
