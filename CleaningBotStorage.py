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
  utils.roomsvisited[4] = 1
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
  utils.roomsvisited[0] = 1
  os.system('cls' if os.name == 'nt' else 'clear')
  if not utils.advanced:
      PrivateWorkshop.basicDes()
  else:
      PrivateWorkshop.fancyDes()
  

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

def itemsInInventory():
    inventorylist = [] 
    for each in utils.inventory.keys():
      inventorylist.append(each)
    return inventorylist

def listItems():
    lst = itemsInhere()
    for each in lst:
        print(each)
    
def examine(obj):
    lst = itemsInhere()
    if obj in lst:
        if itemdictionary[obj][1] == True or itemdictionary[obj][1] == None:
            itemdictionary[obj][0].examine()
    else:
        print("Hmm... {} doesn't seem to be in this room!".format(obj))

def use(obj):
    lst = itemsInhere()
    lst2 = itemsInInventory()
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
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].take(filename)
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))