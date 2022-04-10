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
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'terminal':  [terminal1     , None ]    
}

def basicDes():
    T.Hallway4.basicDes()
         
def fancyDes():
    T.Hallway4.fancyDes()

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    utils.roomsvisited[26] = 1
    if not utils.advanced:
        Server.basicDes()
    else:
        Server.fancyDes()

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    utils.roomsvisited[19] = 1
    if not utils.advanced:
        Hallway3.basicDes()
    else:
        Hallway3.fancyDes()  

def movesouth():
  if not terminal1.locked or utils.cheat:
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    utils.roomsvisited[21] = 1
    if not utils.advanced:
        OrigamiHeadOffice.basicDes()
    else:
        OrigamiHeadOffice.fancyDes()
  else:
    print("The office is locked.")
 
def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    utils.roomsvisited[14] = 1
    if not utils.advanced:
        Hallway5.basicDes()
    else:
        Hallway5.fancyDes()
        
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