# -*- coding: utf-8 -*-
"""
Room#22: A lab for testing robots.
"""
import Item as I
import utils
import BotTesting
#import Puzzle4
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText

itemdictionary = { # [Item, isLocked]

}

def basicDes():
    T.BotTestingObstacleCourse.basicDes()
    if utils.puzzle4 == False:
        Puzzle4.puzzle4()
        utils.puzzle4 = True
         
def fancyDes():
    T.BotTestingObstacleCourse.fancyDes()
    if utils.puzzle4 == False:
        Puzzle4.puzzle4()
        utils.puzzle4 = True
        
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

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary)

