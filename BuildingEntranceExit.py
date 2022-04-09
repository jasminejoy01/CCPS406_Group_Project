# -*- coding: utf-8 -*-
"""
Room#11: The building's side entrance.
"""
import Item as I
import utils
import Hallway1
import OutdoorsMiddle
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")
#utils.roomsvisited[11] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
}

def basicDes():
  if not checkClean():
    T.BuildingEntranceExit.basicDes1()
  else:
    T.BuildingEntranceExit.basicDes2()
     
def fancyDes():
    T.BuildingEntranceExit.fancyDes()

def checkClean():
  for i in range(len(utils.PlayerKeys)):
    if utils.PlayerKeys[i] == 2:
      return True
  return False

def movewest():
    if not checkClean() and not utils.cheat:
      print("The guard at the desk stops me before I can get to the hall. \n 'What are you doing?' she yells, 'Don't you see how filty this room is? I swear, they're so proud of their fancy cleaning bots, you'd think they'd recognize when a job needs doing.''")
    else:
        utils.x = utils.x + 1
        utils.roomsvisited[17] = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        if not utils.advanced:
            Hallway1.basicDes()
        else:
            Hallway1.fancyDes()

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    utils.roomsvisited[5] = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
        OutdoorsMiddle.basicDes()
    else:
        OutdoorsMiddle.fancyDes()


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