# -*- coding: utf-8 -*-
"""
Room#22: A lab for testing robots.
"""
import Item as I
import utils
import BotTesting
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
screwdriver = I.Item("screwdriver", True, False, "A well-worn screwdriver", True, "I'm not sure what to do with this")

itemdictionary = { # [Item, isLocked]
  'screwdriver': [screwdriver,  None]
}

def basicDes():
    T.BotTestingObstacleCourse.basicDes()
         
def fancyDes():
    T.BotTestingObstacleCourse.fancyDes()
        
def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():  
    utils.x = utils.x - 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
      BotTesting.basicDes()   
    else:
      BotTesting.fancyDes()
    print("The construction bot seems to have left...")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)

