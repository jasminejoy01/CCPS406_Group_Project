# -*- coding: utf-8 -*-
"""
Room#16: The building's side entrance.
"""
import Item as I
import utils
import BotTestingObstacle
import Hallway1
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")
blockedDoor = True

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
machinery = I.Item("machinery", False, False, "Some sort of massive, heavy machinery. It's hard to tell what it does.", True, "")
screwdriver = I.Item("screwdriver", True, False, "A well-worn screwdriver", True, "I'm not sure what to do with this")

itemdictionary = { # [Item, isLocked]
  'machinery':    [machinery  , None ],
  'screwdriver': [screwdriver,  None]
}

def basicDes():
    T.BotTesting.basicDes()
          
def fancyDes():
    T.BotTesting.fancyDes()

def movewest():
  if not blockedDoor:
    utils.x = utils.x + 1
    utils.roomsvisited[22] = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
        BotTestingObstacle.basicDes()
    else:
        BotTestingObstacle.fancyDes()
  else:
    print("There is a blockage in front of the door.")
  
def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    utils.roomsvisited[17] = 1
    utils.y = utils.y + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
      Hallway1.basicDes()
    else:
      Hallway1.fancyDes()

def moveeast():
    print("Woops! Can't go that way!")

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

def itemsInInventory():
    inventorylist = []
    if len(utils.inventory) == 0 : 
        return inventorylist
    else:
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

def unlock(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].unlock()
    else:
        print("Hmm... {} cannot be unlocked!".format(obj))

def removeInventory(obj):
    lst = itemsInhere()
    if obj in lst:
        (utils.inventory).remove(obj)
    else:
        print("Hmm... {} is not in inventory!".format(obj))