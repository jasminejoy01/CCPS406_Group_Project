# -*- coding: utf-8 -*-
"""
Room#3: Storage for Origami Bots.
"""

import Item as I
import utils
import OutdoorsSouth
import oriBot as o
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
origamiBot = o.oriBot()

itemdictionary = { # [Item, isLocked]
  'origamibot': [origamiBot, None]
}

def basicDes():
    T.OrigamiBotStorage.basicDes()
    if not utils.inInventory("origamiBot"):
      print("A single origamiBot sits out on a table.")
         
def fancyDes():
    T.OrigamiBotStorage.fancyDes()
    if not utils.inInventory("origamiBot"):
      print("A single origamiBot sits out on a table.")

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
      OutdoorsSouth.basicDes()
    else:
      OutdoorsSouth.fancyDes()

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")

def listItems():
    listitems = (itemdictionary.keys())
    for each in listitems:
        print(each)
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
