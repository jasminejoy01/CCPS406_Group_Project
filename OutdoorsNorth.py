# -*- coding: utf-8 -*-
"""
Room#4: Outdoors North
"""
import Item as I
import utils
import Greenspace
import OutdoorsMiddle
import CleaningBotStorage
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}

def basicDes():
    T.OutdoorNorth.basicDes()
          
def fancyDes():
    T.OutdoorNorth.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    utils.roomsvisited[10] = 1
    if not utils.advanced:
        Greenspace.basicDes()
    else:
        Greenspace.fancyDes()
  
def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    utils.roomsvisited[5] = 1
    if not utils.advanced:
        OutdoorsMiddle.basicDes()
    else:
        OutdoorsMiddle.fancyDes()
   
def moveeast():    
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    utils.roomsvisited[1] = 1
    if not utils.advanced:
      CleaningBotStorage.basicDes()
    else:
      CleaningBotStorage.fancyDes()

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
