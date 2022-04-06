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

filename = 'Hallway6'

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'terminal':  [terminal1     , None ]    
}

def basicDes():
    T.Hallway6.basicDes()
         
def fancyDes():
    T.Hallway6.fancyDes()

def movewest():  
    if utils.advanced == True:
        utils.x = utils.x + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[14] = 1
        Hallway5.basicDes()
    else:
        utils.x = utils.x + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[14] = 1
        Hallway5.fancyDes()

def movenorth(): 
    if utils.advanced == True:
        utils.y = utils.y - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[7] = 1
        Storage.basicDes()

    else:
        utils.y = utils.y - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[7] = 1
        Storage.fancyDes()


def movesouth():
    if utils.advanced == True:
        utils.y = utils.y + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[9] = 1
        Exit.basicDes()
    else:
        utils.y = utils.y + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        Exit.fancyDes()
        utils.roomsvisited[9] = 1

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