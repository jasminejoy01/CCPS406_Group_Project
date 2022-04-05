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
#utils.roomsvisited[1] = 1

## Items in Room
##################

#name,  canTake, inInventory, description, interactable, useText
broom = I.Item("broom", False, False, "an ordinary broom", True, "I'm sweeping")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , False],
   'broom':     [broom     , None ],
  'terminal':  [terminal1     , None ]           
}

def basicDes():
    print("[Housekeeping Storage Bay] \n This room is well lit and sparkling clean. There are robots connected to wires which feed into monitors on either side of them; a familiar sight. \n There are shelves and storage containers covering a majority of the room. They’re full of storage racks containing bleach, soap, and other types of cleaning supplies organized by product. \n There are brooms neatly stacked on a storage rack near the door to the West. \n Beside the door is another NFC Terminal identical to the first one found in the other room.")

def fancyDes():
    print("[Housekeeping Storage Bay] \n Returning back to this room, I realize how much cleaner it is compared to the rest of the compound; not a speck of dust anywhere. \n There are shelves and storage containers covering a majority of the room. There's less items in here than when I had woken up. There are less brooms on the storage rack near the door, I remember which of the missing brooms was the one I took.")
  
def movewest(): 
    if utils.advanced == True:
        utils.x = utils.x + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        OutdoorsNorth.basicDes()
        utils.roomsvisited[4] = 1
    else:
        utils.x = utils.x + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        OutdoorsNorth.fancyDes()
        utils.roomsvisited[4] = 1
  

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def moveeast():
    if utils.advanced == True:
        utils.x = utils.x - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[0] = 1
        PrivateWorkshop.basicDes()
    else:
        utils.x = utils.x - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[0] = 1
        PrivateWorkshop.fancyDes()



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