# -*- coding: utf-8 -*-
"""
Room#2: Storage for Cleaning Bots
"""
import Item as I
import utils

#print("You're in the Cleaning Bot Storage.")

utils.roomsvisited[1] = 1

## Items in Room
##################

#name, islocked, canTake, inInventory, description, interactable, useText, unlockText
#nullItem = I.Item("", False, False, False, "", False, "", "")
broom = I.Item("broom", False, False, False, "an ordinary broom", True, "I'm sweeping", "")
terminal = I.Item("terminal", True, False, False, "The terminal reads \n\'LOCKED\'", True, "It seems to require an NFC key", "You interact with the NFC terminal and the screen changes: \n\‘UNLOCKED\’")
paper = I.Item("paper", False, True, False, "It reads: April 20, 2020. Head of Robotics at [company], [name], has been awarded for remarkable contribution to science for her creation of a highly adaptable cleaning robot. At the age of 28, she is one of the youngest scientists to ever achieve such an acomplishment. We're excited to see what she does next.", True, "It reads: April 20, 2020. Head of Robotics at [company], [name], has been awarded for remarkable contribution to science for her creation of a highly adaptable cleaning robot. At the age of 28, she is one of the youngest scientists to ever achieve such an acomplishment. We're excited to see what she does next.", "")
door = I.Item("door", True, False, False, "", True, "", "")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , False],
   'broom':     [broom     , None ],
   'terminal':  [terminal  , True ],               
   'paper':     [paper      , None ],
   'door':      [door      , True ]
}

def basicDes():
    print("Storage for Cleaning Bots")

def fancyDes():
    print("This room is well lit and sparkling clean. There are robots connected to wires which feed into monitors on either side of them; it’s a familiar sight. There are shelves and storage containers covering a majority of the room. They’re full of containers containing bleach, soap, and other types of cleaning supplies organized by product. There are brooms neatly stacked on a storage rack near the door to the West. Beside the West door is another NFC Terminal identical to the first one found in the other room. There is an East door back to the private workshop.", "This room is well lit and sparkling clean. There are robots connected to wires which feed into monitors on either side of them; it’s a familiar sight. There are shelves and storage containers covering a majority of the room. They’re full of containers containing bleach, soap, and other types of cleaning supplies organized by product. There are brooms neatly stacked on a storage rack near the door to the West. Beside the West door is another NFC Terminal identical to the first one found in the other room. There is an East door back to the private workshop.")

def movewest():
    utils.x = utils.x + 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving outdoors!")

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y + 0
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Private workshop!")

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