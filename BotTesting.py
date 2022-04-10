# -*- coding: utf-8 -*-
"""
Room#16: The building's side entrance.
"""
import Item as I
import utils
import BotTestingObstacle
import Hallway1
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")
blockedDoor = True

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
machinery = I.Item("machinery", False, False, "Some sort of massive, heavy machinery. It's hard to tell what it does.", True, "")
screwdriver = I.Item("screwdriver", True, False, "A well-worn screwdriver", True, "I'm not sure what to do with this")

itemdictionary = { # [Item, isLocked]
  'machinery':    [machinery  , None ],
  'screwdriver': [screwdriver,  None]
}

def basicDes():
    T.BotTesting.basicDes()
          
def fancyDes():
    T.BotTesting.fancyDes()

def movewest():
  if not blockedDoor:
    utils.x = utils.x + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
        BotTestingObstacle.basicDes()
    else:
        BotTestingObstacle.fancyDes()
  else:
    print("There is a blockage in front of the door.")
  
def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    utils.y = utils.y + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
      Hallway1.basicDes()
    else:
      Hallway1.fancyDes()

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

