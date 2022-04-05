# -*- coding: utf-8 -*-
"""
Room#2: Storage for Cleaning Bots
"""
import Item as I
import utils
import PrivateWorkshop
import OutdoorsNorth

#print("You're in the Cleaning Bot Storage.")
filename = 'CleaningBotStorage'

## Items in Room
##################

#name,  canTake, inInventory, description, interactable, useText
broom = I.Item("broom", False, False, "an ordinary broom", True, "I'm sweeping")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , False],
   'broom':     [broom     , None ],
   'terminal':  [terminal1 , None ]           
}

def basicDes():
    print("Storage for Cleaning Bots")

def fancyDes():
    print("This room is well lit and sparkling clean. There are robots connected to wires which feed into monitors on either side of them; it’s a familiar sight. There are shelves and storage containers covering a majority of the room. They’re full of containers containing bleach, soap, and other types of cleaning supplies organized by product. There are brooms neatly stacked on a storage rack near the door to the West. Beside the West door is another NFC Terminal identical to the first one found in the other room. There is an East door back to the private workshop.", "This room is well lit and sparkling clean. There are robots connected to wires which feed into monitors on either side of them; it’s a familiar sight. There are shelves and storage containers covering a majority of the room. They’re full of containers containing bleach, soap, and other types of cleaning supplies organized by product. There are brooms neatly stacked on a storage rack near the door to the West. Beside the West door is another NFC Terminal identical to the first one found in the other room. There is an East door back to the private workshop.")

def movewest(): 
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[4] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            OutdoorsNorth.basicDes()
            utils.roomsvisited[4] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[4] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            OutdoorsNorth.fancyDes()
            utils.roomsvisited[4] = 1
        else:
            print("The door is locked.")    
    

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def moveeast():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[0] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            PrivateWorkshop.basicDes()
            utils.roomsvisited[0] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[0] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            PrivateWorkshop.fancyDes()
            utils.roomsvisited[0] = 1
        else:
            print("The door is locked.")    

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
    lst = itemsInInventory()
    if obj in lst:
        (utils.inventory).drop(obj)
    else:
        print("Hmm... {} is not in inventory!".format(obj))