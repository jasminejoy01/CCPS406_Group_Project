# -*- coding: utf-8 -*-
"""
Room#1: Private Workshop
"""
import Item as I
import utils

#print("You're in the Private Workshop.")

utils.roomsvisited[0] = 1

## Items in Room
##################

#name, islocked, canTake, inInventory, description, interactable, useText, unlockText
nullItem = I.Item("", False, False, False, "", False, "", "")
computer1 = I.Computer("computer", True, False, False, "A fairly modern PC. Some sticky notes line the edges of the monitor. A keyboard sits in front of it on the desk.", True, "", "")
keyboard = I.Item("keyboard", None, False, False, "A beat up old keyboard. There's a note sitcking out from under it.", True, "A beat up old keyboard. There's a note sitcking out from under it.", "")
note = I.Item("note", None, True, False, "It reads: 'If I forget again: Initials Birth year Lucky number, no spaces. PS: create a better password.'", True, "It reads: 'If I forget again: Initials Birth year Lucky number, no spaces. PS: create a better password.'", "")
trash = I.Item("trash", None, False, False, "Inside the bin, there is a piece of paper.", True, "I could take the paper out of it", "")
door = I.Item("door", True, False, False, "", True, "", "")

itemdictionary = { # [Item, isLocked]
   'nullItem': [nullItem  , False],
   'computer': [computer1 , True ],
   'keyboard': [keyboard  , None ],               
   'note':     [note      , None ],
   'trash':    [trash     , None ],
   'door':     [door      , True ]
}

def basicDes():
    print("A small room with a computer on a desk. There is a door to the West.")

def fancyDes():
    print("There room has no windows. There is a door to the left.")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Cleaning Bot Storage", utils.x, utils.y)

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def moveeast():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

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