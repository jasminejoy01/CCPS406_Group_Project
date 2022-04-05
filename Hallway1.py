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

#print("You're in the Hallway#1.")
filename = 'Hallway1'
utils.roomsvisited[17] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],

}

def basicDes():
    print("The hall continues south. The security desk is East, and there are doors North and West.")

def fancyDes():
    print("")

def movewest():
    if utils.advanced:
      PrototypeWorkshop.fancyDes()
    else:
      PrototypeWorkshop.basicDes()
    utils.x = utils.x + 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Prototype Shop!")

def movenorth():
    utils.y = utils.y - 1
    if utils.advanced:
      BotTesting.fancyDes()
    else:
      BotTesting.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Bot Testing Simple Tasks")

def movesouth():
    utils.y = utils.y + 1
    Hallway2.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're  moving into Hallway 2!")

def moveeast():
    utils.x = utils.x - 1
    if utils.advanced:
      BuildingEntranceExit.fancyDes()
    else:
      BuildingEntranceExit.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back into Building Entrance/Exit.")

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

def itemsInInventory():
    inventorylist = []
    if len(inventorylist) == 0 : 
        return inventorylist
    else:
        for each in utils.keys():
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