# -*- coding: utf-8 -*-
"""
Room#8: Hallway 6
"""
import Item as I
import utils
import Storage
import Exit
import Hallway5
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
    T.Hallway6.basicDes()
    if not utils.blockedDoor:
      print("The construction bot is here, wearing... Is that a tarp? It has a hole cut in the middle to fit over the constructionBot's head like a poncho. It also has a hat.")
         
def fancyDes():
    T.Hallway6.fancyDes()
    if not utils.blockedDoor:
      print("The construction bot is here, wearing... Is that a tarp? It has a hole cut in the middle to fit over the constructionBot's head like a poncho. It also has a large green sunhat.")

def movewest():  
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    if not utils.advanced:
        Hallway5.basicDes()
    else:
        Hallway5.fancyDes()

def movenorth(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    if not utils.advanced:
        Storage.basicDes()
    else:
        Storage.fancyDes()


def movesouth():
  if utils.EMgate:
    print("I shouldn't try to leave yet. The electromagnetic security gate is still up. I'd be fried!")
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        Exit.basicDes()
    else:
        Exit.fancyDes()

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
