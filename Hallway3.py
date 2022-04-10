# -*- coding: utf-8 -*-
"""
Room#19: Hallway 3
"""
import Item as I
import utils
import CreatorOffice
import Hallway2
import ConstructionHeadOffice
import Hallway4
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal3 = I.Terminal(3)#Construction office terminal

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal3 , None ]
}

def basicDes():
    T.Hallway3.basicDes()
         
def fancyDes():
    T.Hallway3.fancyDes()


def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
        CreatorOffice.basicDes()
        CreatorOffice.creatorIntro()
    else:
        CreatorOffice.fancyDes()
        CreatorOffice.meetAgain()

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    if not utils.advanced:
        Hallway2.basicDes()
    else:
        Hallway2.fancyDes()  

def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        Hallway4.basicDes()
    else:
        Hallway4.fancyDes()
 
def moveeast():
  if not terminal3.locked or utils.cheat:
    utils.x = utils.x - 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
        ConstructionHeadOffice.basicDes()
    else:
        ConstructionHeadOffice.fancyDes()
  else:
    print("The door is locked.")
        
def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
