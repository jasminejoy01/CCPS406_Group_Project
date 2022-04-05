# -*- coding: utf-8 -*-
"""
Room#16: The building's side entrance.
"""
import Item as I
import utils
import BotTestingObstacle
import Hallway1

#print("You're in the Bot Testing Room.")
filename = 'BotTesting'
#utils.roomsvisited[16] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)
screwdriver = I.Item("screwdriver", True, False, "A well-worn screwdriver", True, "")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'terminal':  [terminal1     , None ],
  'screwdriver': [screwdriver,   None]
}

def basicDes():
    print("[Robotics Testing Facility - Basic Functions] \n I find myself in a rather large and spacious room. \n There are tables scattered throughout the room; it appears as if there are multiple workstations with varying activities. A screwdriver sits on one of them.\n To the west is a door with a sign above it; I can't read it because there is havy machinery blocking my view. \n There's a robot hooked up to a terminal, similar to the one from the House Keeping Storage Bay, however it's much larger than me and the other robots I've seen. \n To the East is the door that leads back to [Hallway - Section 1]")

def fancyDes():
    print("[Robotics Testing Facility – Basic Functions] \n I'm back inside the Robotics Testing Facility, the room that has all the types of tests placed on different tables. \n To the West is [Bot Testing - Obstacle Course] \n To the East is [Hallway - Section 1]")

def movewest():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[22] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
              utils.x = 0
            if utils.y < 0:
              utils.y = 0
            BotTestingObstacle.basicDes()
            utils.roomsvisited[22] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[16] == 1:
            utils.x = utils.x + 1
            BotTestingObstacle.fancyDes()
        else:
            print("The door is locked.")    


def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False:
            utils.y = utils.y + 1
            Hallway1.basicDes()
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False:
            utils.y = utils.y + 1
            Hallway1.fancyDes()
        else:
            print("The door is locked.")    
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0

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