# -*- coding: utf-8 -*-
"""
Room#5: Outside space between the storage building and main lab
"""
import Item as I
import utils
import OutdoorsNorth
import OutdoorsSouth
import ConstructionBotStorage
import BuildingEntranceExit
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal3 = I.Terminal(3)

itemdictionary = { # [Item, isLocked]
  'terminal':   [terminal3, True]
}

def basicDes():
    T.OutdoorMiddle.basicDes()
          
def fancyDes():
    T.OutdoorMiddle.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
        BuildingEntranceExit.basicDes()
    else:
        BuildingEntranceExit.fancyDes()
 
def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    #utils.roomvisited[4] = 1
    if not utils.advanced:
      OutdoorsNorth.basicDes()
    else:
      OutdoorsNorth.fancyDes()
 
def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
      OutdoorsSouth.basicDes()
    else:
      OutdoorsSouth.fancyDes()

def moveeast():
  if not terminal3.locked or utils.cheat:
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
      ConstructionBotStorage.basicDes()
    else:
        ConstructionBotStorage.fancyDes()
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
