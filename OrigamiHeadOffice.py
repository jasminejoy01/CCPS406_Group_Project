# -*- coding: utf-8 -*-
"""
Room#21: Head of Origami Office.
"""
import Item2 as I2
import Item as I
import utils
import Hallway4
import puzzle6
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")
#utils.roomsvisited[21] = 1


## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
OrigamiKey = I.Item("", True, False,  "", False, "")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'OrigamiKey' : [OrigamiKey, None]
}

def basicDes():
    T.OrigamiHeadOffice.basicDes()
         
def fancyDes():
    T.OrigamiHeadOffice.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    
    if utils.origamiHeadChecker == False: 
        puzzle6.main()
        utils.origamiHeadChecker == True
     
    if 'OrigamiKey' not in utils.inventory.keys():
        I2.Origami_Office.item_add()
        
    if not utils.advanced:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[20] == 1:
            utils.y = utils.y - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway4.basicDes()
            utils.roomsvisited[20] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[20] == 1:
            utils.y = utils.y - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway4.fancyDes()
            utils.roomsvisited[20] = 1
        else:
            print("The door is locked.")   

def movesouth():
    print("Woops! Can't go that way!")

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