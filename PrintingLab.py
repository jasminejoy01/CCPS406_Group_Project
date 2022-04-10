# -*- coding: utf-8 -*-
"""
Room#24: 3D Printing Lab
"""
import Item as I
import utils
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
    T.PrintingLab.basicDes()
    if utils.blockedDoor:
      print("One of the printers has a large tarp over it. It looks fairly secure, so I shouldn't bother with it.")
    else:
      print("It appears that a covering has been ripped off of one of the printers. It must've taken a lot of force.")
         
def fancyDes():
    T.PrintingLab.fancyDes()
    if utils.blockedDoor:
      print("One of the printers has a large tarp over it. It looks fairly secure, so I shouldn't bother with it.")
    else:
      print("It appears that a covering has been ripped off of one of the printers. It must've taken a lot of force.")

    
def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
        Hallway2.basicDes()
    else:
        Hallway2.fancyDes()

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
