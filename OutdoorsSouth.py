# -*- coding: utf-8 -*-
"""
Room#6: Outside space between the storage building and main lab
"""
import Item as I
import utils
import OrigamiBotStorage
import OutdoorsMiddle
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
terminal2 = I.Terminal(2)

itemdictionary = { # [Item, isLocked]
  'terminal':  [terminal2     , None ]    
}

def basicDes():
    T.OutdoorSouth.basicDes()
          
def fancyDes():
    T.OutdoorSouth.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    utils.roomsvisited[5] = 1
    if not utils.advanced:
        OutdoorsMiddle.basicDes()
    else:
        OutdoorsMiddle.fancyDes()  

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
  if not terminal2.locked or utils.cheat:
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    utils.roomsvisited[3] = 1
    if not utils.advanced:
        OrigamiBotStorage.basicDes()
    else:
        OrigamiBotStorage.fancyDes()
  else:
    print("The door is locked. I'll have to unlock it by using the terminal.")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary)
