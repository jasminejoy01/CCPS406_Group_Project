# -*- coding: utf-8 -*-
"""
Room#5: Outside space between the storage building and main lab
"""
import Item as I
import utils
import OutdoorsNorth
import OutdoorsSouth
import ConstructionBotStorage
import BuildingEntranceExit

#print("You've stepped into the Middle corridoors outside.")

utils.roomsvisited[5] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],

}

def basicDes():
    print("The paved outdoor area continues North and South. There are doors to the East and West.")

def fancyDes():
    print("")

def movewest():
    utils.x = utils.x + 1
    if utils.advanced:
      BuildingEntranceExit.fancyDes()
    else:
      BuildingEntranceExit.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("Now, you're moving to Greenspace break area!", utils.x, utils.y)

def movenorth():
    utils.y = utils.y - 1
    OutdoorsNorth.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Outdoors (north)!", utils.x, utils.y)

def movesouth():
    utils.y = utils.y + 1
    OutdoorsSouth.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Outdoors (middle)!", utils.x, utils.y)

def moveeast():
    utils.x = utils.x - 1
    if utils.advanced:
      ConstructionBotStorage.fancyDes()
    else:
      ConstructionBotStorage.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Construction Bot Storage!", utils.x, utils.y)

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

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
    if obj in lst:
        if itemdictionary[obj][1] == True:
            print("It's Locked!")
        else:
            itemdictionary[obj][0].use()
    else:
        print("Hmm... {} can't use an object that's not in this room! You can check your inventory to look for items to use".format(obj))
 
def take(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].take()
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