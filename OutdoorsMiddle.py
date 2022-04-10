# -*- coding: utf-8 -*-
"""
Room#5: Outside space between the storage building and main lab
"""
import Item as I
import utils
import OutdoorsNorth
import OutdoorsSouth
import ConstructionBotStorage
import BuildingEntranceExit
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal3 = I.Terminal(3)

itemdictionary = { # [Item, isLocked]
  'terminal':   [terminal3, True]
}

def basicDes():
    T.OutdoorMiddle.basicDes()
          
def fancyDes():
    T.OutdoorMiddle.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    utils.roomsvisited[11] = 1
    if not utils.advanced:
        BuildingEntranceExit.basicDes()
    else:
        BuildingEntranceExit.fancyDes()
 
def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    utils.roomsvisited[4] = 1
    if not utils.advanced:
      OutdoorsNorth.basicDes()
    else:
      OutdoorsNorth.fancyDes()
 
def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    utils.roomsvisited[6] = 1
    if not utils.advanced:
      OutdoorsSouth.basicDes()
    else:
      OutdoorsSouth.fancyDes()

def moveeast():
  if not terminal3.locked or utils.cheat:
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    utils.roomsvisited[2] = 1
    if not utils.advanced:
      ConstructionBotStorage.basicDes()
    else:
        ConstructionBotStorage.fancyDes()
  else:
    print("The door is locked. I'll have to unlock it by using the terminal.")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    lst = itemdictionary.keys()
    #print(obj)
    if obj in lst:
        if itemdictionary[obj][1] == True or itemdictionary[obj][1] == None:
            itemdictionary[obj][0].examine()
    else:
        print("Hmm... {} doesn't seem to be in this room!".format(obj))

def use(obj):
    lst = itemdictionary.keys()
    lst2 = utils.inventory.keys()
    #print(lst2)
    if obj in lst and obj not in lst2:
        itemdictionary[obj][0].use()
    elif obj in lst2 and obj not in lst:
        where = utils.inventory[obj]
        __import__(where).use(obj)
    elif obj in lst and obj in lst2:
        itemdictionary[obj][0].use()
    else:
        print("Hmm... {} can't use an object that's not in this room! You can check your inventory to look for items to use".format(obj))
 
def take(obj):
    if obj in itemdictionary.keys():
        itemdictionary[obj][0].take(filename)
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))
