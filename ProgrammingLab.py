# -*- coding: utf-8 -*-
"""
Room#12: Programming Lab"
"""
import Item as I
import utils
import Hallway2
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)
computer = I.Item("", False, False, "", False, "Hmm.. let's see if I can access people's schedules here... ")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],  
  'computer':  [ computer  , True ]
}

def basicDes():
    T.ProgrammingLab.basicDes()
         
def fancyDes():
    T.ProgrammingLab.fancyDes()

def movewest():
    #This should not be in movewest! This doesn't make sense here!
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    utils.roomsvisited[18] = 1
    if not utils.advanced:
        Hallway2.basicDes()
    else:
        Hallway2.fancyDes()
 
def movenorth():
    print("Woops! Can't go that way!")

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
    room.take(obj, itemdictionary)
