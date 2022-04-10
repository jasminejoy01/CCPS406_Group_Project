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
         
def fancyDes():
    T.Hallway6.fancyDes()

def movewest():  
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    utils.roomsvisited[14] = 1
    if not utils.advanced:
        Hallway5.basicDes()
    else:
        Hallway5.fancyDes()

def movenorth(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    utils.roomsvisited[7] = 1
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
    utils.roomsvisited[9] = 1
    if not utils.advanced:
        Exit.basicDes()
    else:
        Exit.fancyDes()

def moveeast():
    print("Woops! Can't go that way!")

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
