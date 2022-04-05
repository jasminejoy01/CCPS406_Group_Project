# -*- coding: utf-8 -*-
"""
Room#3: Storage for Origami Bots.
"""

import Item as I
import utils
import OutdoorsSouth
import oriBot as o

#print("You're in the Origami Bot Storage.")
filename = 'OrigamiBotStorage'
#utils.roomsvisited[3] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)
origamiBot = o.oriBot()

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ],
  'origamibot': [origamiBot, None]
}

def basicDes():
    print("[Abstract Solutions Storage Bay] \n Despite it's unique exterior, the inside of this storage bay is identical to the one for Housekeeping. \n The shelves line the walls and they're full of different machine parts. A single origamibot lies on the table.")

def fancyDes():
    print("[Abstract Solutions Storage Bay] \n Coming back, I realize how intricate these machine parts are on the shelves; they're all capable of folding in different directions. \n What interesting pieces of technology.")

def movewest():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[6] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            OutdoorsSouth.basicDes()
            utils.roomsvisited[6] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[6] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            OutdoorsSouth.fancyDes()
            utils.roomsvisited[6] = 1
        else:
            print("The door is locked.")   


def movenorth():
    print("Woops! Can't go that way!")

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