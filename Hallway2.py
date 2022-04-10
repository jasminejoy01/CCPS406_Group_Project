# -*- coding: utf-8 -*-
"""
Room#18: Hallway 2
"""
import Item as I
import utils
import Hallway1
import PrintingLab
import ProgrammingLab
import Hallway3
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
    T.Hallway2.basicDes()
         
def fancyDes():
    T.Hallway2.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
      if utils.alarmOn:
        PrintingLab.basicDes1()
      else:
        PrintingLab.basicDes2()
    else:
      if utils.alarmOn:
        PrintingLab.fancyDes2()
      else:
        PrintingLab.fancyDes2()

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    if not utils.advanced:
        Hallway1.basicDes()
    else:
        Hallway1.fancyDes()  

def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        Hallway3.basicDes()
    else:
        Hallway3.fancyDes()
 
def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
        ProgrammingLab.basicDes()
    else:
        ProgrammingLab.fancyDes()

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
