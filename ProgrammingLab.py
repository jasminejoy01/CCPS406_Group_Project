# -*- coding: utf-8 -*-
"""
Room#12: Programming Lab"
"""
import Item as I
import utils
import Hallway2

#print("You're in the Programming Lab.")
filename = 'ProgrammingLab'
#utils.roomsvisited[12] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)
computer = I.Item("", False, False, "", False, "Hmm.. let's see if I can access people's schedules here... ")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],  
  'computer':  [ computer  , True ]
}


def basicDes():
    print("here is a door to the West.")

def fancyDes():
    print("")

def movewest():
    if utils.programminglabOccupied == False:
        computer.getSchedule()
        utils.origamiHeadChecker == False
    else:
        print("You need to vacate the Programming Lab to access a computer.")

    terminal1.locked = False
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[18] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            utils.roomsvisited[18] = 1
            Hallway2.basicDes()
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[18] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            utils.roomsvisited[18] = 1
            Hallway2.fancyDes()
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