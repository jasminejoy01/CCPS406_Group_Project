# -*- coding: utf-8 -*-
"""
Room#21: Head of Origami Office.
"""

import Item as I
import utils
import Hallway4

#print("You're in the Head of Origami Office.")
filename = 'OrigamiHeadOffice'
#utils.roomsvisited[21] = 1

if utils.origamiHeadChecker == False:
    import Puzzle6
    Puzzle6.main()
    utils.origamiHeadChecker == True

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
OrigamiKey = I.Item("", True, False,  "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'OrigamiKey' : [OrigamiKey, None],
  'terminal':  [terminal1     , None ]  
}

def basicDes():
    print("[Abstract Solutions Office] \n The first thing I notice as I walk through the door is the vast amount of small animal figures that cover the room. \n Detailed paper recreations of animals are on display on lit-up display shelves, sitting across counters, and covering the lone desk at the back of the room. \n Behind the desk is a large framed picture; I don’t think I've ever seen anything like this before, it looks similar to the foliage I saw outside. \n To the North is the door that leads back into [Hallway - Section 4]")

def fancyDes():
    print("[Abstract Solutions Office] \n Back to the room filled with 'Origami'. \n The paper recreations of animals are still on display on the lit-up display shelves.\n Seeing these recreations again, it's interesting to think that I value the way they look more now than I had when I first came, but nothing changed about them. \n The way each animal was created with its own specific paper, and that some bigger models have multiple, different coloured paper used to create it. \n To the North is [Hallway - Section 4]")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    if utils.advanced == True:
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