# -*- coding: utf-8 -*-
"""
Room#20: Hallway 4
"""
import Item as I
import utils
import Server
import OrigamiHeadOffice
import Hallway5
import Hallway3
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal4 = I.Terminal(4)#Will be unlocked when Dr Yami leaves her office

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'terminal':  [terminal4     , None ]    
}

def basicDes():
    T.Hallway4.basicDes()
         
def fancyDes():
    T.Hallway4.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
        Server.basicDes()
    else:
        Server.fancyDes()

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    if not utils.advanced:
        Hallway3.basicDes()
    else:
        Hallway3.fancyDes()  

def movesouth():
  if not terminal4.locked or utils.cheat:
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        OrigamiHeadOffice.basicDes()
    else:
        OrigamiHeadOffice.fancyDes()
  else:
    print("The office is locked.")
 
def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
        Hallway5.basicDes()
    else:
        Hallway5.fancyDes()
        
def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary)
