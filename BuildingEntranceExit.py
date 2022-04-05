# -*- coding: utf-8 -*-
"""
Room#11: The building's side entrance.
"""
import Item as I
import utils
import Hallway1
import OutdoorsMiddle

#print("You're in the building's side entrance.")
filename = 'BuildingEntranceExit'
utils.roomsvisited[11] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],

}

def basicDes():
    print("[Main Facility Entrance] (Before cleaning the dirt) \n I'm standing near the Security Checkpoint, there is a security guard at the desk watching the screens in front of her. \n Looking around, I see that there are trails of dirt and debris following the path that the employees take to go in and out of the building.") 
  
def fancyDes():
    print("[Main Facility Entrance] (After cleaning the dirt) \n I'm back near the Security Checkpoint for the Storage Bays. The same security guard is at the desk watching the screens in front of her. \n There are no heavy trails of dirt on the path of the employees, I suspect that she won't bother me about having to clean anything before continuing past.")
  
def movewest():
    clean = False  
    for i in range(len(utils.PlayerKeys)):
      if utils.PlayerKeys[i] == 2:
        clean = True
    if not clean and not utils.cheat:
      print("The guard at the desk stops me before I can get to the hall. \n 'What are you doing?' she yells, 'Don't you see how filty this room is? I swear, they're so proud of their fancy cleaning bots, you'd think they'd recognize when a job needs doing.''")
    else: 
      utils.x = utils.x + 1
      Hallway1.basicDes()
      if utils.x < 0:
          utils.x = 0
      if utils.y < 0:
          utils.y = 0
    #print("You're moving to the Hallway#1 !")

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    OutdoorsMiddle.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Outdoor (middle)!")

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