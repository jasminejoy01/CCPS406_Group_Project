# -*- coding: utf-8 -*-
"""
Room#2: Storage for Cleaning Bots
"""
import Item as I
import Item2 as I2
import utils
import PrivateWorkshop
import OutdoorsNorth
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
broom = I.Item("broom", True, False, "an ordinary broom", True, "I'm sweeping")

itemdictionary = { # [Item, isLocked]
   'broom'   :     [broom     , None ]     
}

def basicDes():
    T.CleaningBotStorage.basicDes()
          
def fancyDes():
    T.CleaningBotStorage.fancyDes()

def movewest(): 
  utils.x = utils.x + 1
  os.system('cls' if os.name == 'nt' else 'clear')
  if not utils.advanced:
        OutdoorsNorth.basicDes()       
  else:       
        OutdoorsNorth.fancyDes()

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
  utils.x = utils.x - 1 
  #utils.roomvisited[0] = 1
  os.system('cls' if os.name == 'nt' else 'clear')
  if not utils.advanced:
      PrivateWorkshop.basicDes()
  else:
      PrivateWorkshop.fancyDes()
  
def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)

