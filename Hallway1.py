# -*- coding: utf-8 -*-
"""
Room#17: Hallway 1
"""
import Item as I
import utils
import PrototypeWorkshop
import BotTesting
import BuildingEntranceExit
import Hallway2
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
  'terminal':  [terminal1     , None ]   
}

def basicDes():
    T.Hallway1.basicDes()
         
def fancyDes():
    T.Hallway1.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    utils.roomsvisited[23] = 1
    if not utils.advanced:
        PrototypeWorkshop.basicDes()
    else:
        PrototypeWorkshop.fancyDes()

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    utils.roomsvisited[16] = 1
    if not utils.advanced:
        BotTesting.basicDes()
    else:
        BotTesting.fancyDes()  

def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    utils.roomsvisited[18] = 1
    if not utils.advanced:
        Hallway2.basicDes()
    else:
        Hallway2.fancyDes()
 
def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    utils.roomsvisited[11] = 1
    if not utils.advanced:
        BuildingEntranceExit.basicDes()
    else:
        BuildingEntranceExit.fancyDes()

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
    #print(obj)
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