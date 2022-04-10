# -*- coding: utf-8 -*-
"""
Room#11: The building's side entrance.
"""
import Item as I
import utils
import Hallway1
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
#   'nullItem': [nullItem  , None],
}

def basicDes():
  if not utils.cleanHall:
    T.BuildingEntranceExit.basicDes1()
  else:
    T.BuildingEntranceExit.basicDes2()
     
def fancyDes():
    T.BuildingEntranceExit.fancyDes()

def movewest():
    if not utils.cleanHall and not utils.cheat:
      print("The guard at the desk stops me before I can get to the hall. \n 'What are you doing?' she yells, 'Don't you see how filty this room is? I swear, they're so proud of their fancy cleaning bots, you'd think they'd recognize when a job needs doing.''")
    else:
        utils.x = utils.x + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        if not utils.advanced:
            Hallway1.basicDes()
        else:
            Hallway1.fancyDes()

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
        OutdoorsMiddle.basicDes()
    else:
        OutdoorsMiddle.fancyDes()

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)

