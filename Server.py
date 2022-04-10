# -*- coding: utf-8 -*-
"""
Room#26: Server room
"""
import Item as I
import Item2 as I2
import utils
import Hallway4
import time
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}

def basicDes():
    T.ServerRoom.basicDes()
    if utils.securityPuzzleCheck == False:
        I2.ServerRoom.smokealarm()

def fancyDes():
    T.ServerRoom.basicDes()
    if utils.securityPuzzleCheck == False:
        I2.ServerRoom.smokealarm()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    utils.roomsvisited[20] = 1
    if not utils.advanced:
      Hallway4.basicDes() 
    else:
      Hallway4.fancyDes()


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
