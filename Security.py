# -*- coding: utf-8 -*-
"""
Room#15: Security Office
"""
#Not actually accessible to the player, might delete this file

import Item as I
import utils
import Hallway5
import time
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, islocked, canTake, inInventory, description, interactable, useText, unlockText
#nullItem = I.Item("", False, False, False, "", False, "", "")

itemdictionary = { # [Item, isLocked]

}

def basicDes():
    T.Security.basicDes()
         
def fancyDes():
    T.Security.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():  
  if utils.cheat == True or terminal1.locked == False:
    utils.y = utils.y + 1
    if not utils.advanced:
      Hallway5.basicDes()
    else:
      Hallway5.fancyDes()
  else:
    print("The door is locked.")   

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
