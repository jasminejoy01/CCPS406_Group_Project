# -*- coding: utf-8 -*-
"""
Room#4: Outdoors North
"""
import Item as I
import utils
import Greenspace
import OutdoorsMiddle
import CleaningBotStorage

#print("You've stepped outside into the North corridoors.")

utils.roomsvisited[4] = 1

itemshere = []

def basicDes():
    print("Outside space between the storage building and main lab")

def fancyDes():
    print("The open paved area continues South. There is a grassy area with picnic benches to the the West.")

# -*- coding: utf-8 -*-
"""
Room#4: Outdoors North
"""
import Item as I
import utils

utils.roomsvisited[4] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],

}

def basicDes():
    print("Outside space between the storage building and main lab")

def fancyDes():
    print("The open paved area continues South. There is a grassy area with picnic benches to the the West.")

def movewest():
    utils.x = utils.x + 1
    if utils.advanced:
      Greenspace.fancyDes()
    else:
      Greenspace.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("Now, you're moving to Greenspace break area!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    utils.x = utils.x + 0
    utils.y = utils.y + 1
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Outdoors (middle)!", utils.x, utils.y)

def moveeast():
    utils.x = utils.x - 1
    if utils.advanced:
      CleaningBotStorage.fancyDes()
    else:
      CleaningBotStorage.basicDes()
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Cleaning Bot Storage!", utils.x, utils.y)

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