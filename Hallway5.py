# -*- coding: utf-8 -*-
"""
Room#14: Hallway 5
"""
import Item as I
import utils
import Hallway4
import Security
import Hallway6
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
    T.Hallway5.basicDes()
         
def fancyDes():
    T.Hallway5.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
        Hallway4.basicDes()
    else:
        Hallway4.fancyDes()

def movenorth():
    print("Woops! Can't go that way!") 

def movesouth():
    print("Only guards are allowed in the security office. I'd definitely be noticed.")
 
def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
        Hallway6.basicDes()
    else:
        Hallway6.fancyDes()
        
def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary)
