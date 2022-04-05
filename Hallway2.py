# -*- coding: utf-8 -*-
"""
Room#18: Hallway 2
"""
import Item as I
import utils
import Hallway1
import PrintingLab
import ProgrammingLab
import Hallway3

#print("You're in the Hallway#2.")
filename = 'Hallway2'
#utils.roomsvisited[18] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'terminal':  [terminal1     , None ]    
}

def basicDes():
    print("The hall continues North and South. There are doors East and West.")

def fancyDes():
    print("")

def movewest():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[24] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            PrintingLab.basicDes()
            utils.roomsvisited[24] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[24] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            PrintingLab.fancyDes()
            utils.roomsvisited[24] = 1
        else:
            print("The door is locked.")    

def movenorth():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[17] == 1:
            utils.y = utils.y - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway1.basicDes()
            utils.roomsvisited[17] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[17] == 1:
            utils.y = utils.y - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway1.fancyDes()
            utils.roomsvisited[17] = 1
        else:
            print("The door is locked.")    

def movesouth():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[19] == 1:
            utils.y = utils.y + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway3.basicDes()
            utils.roomsvisited[19] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[19] == 1:
            utils.y = utils.y + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway3.fancyDes()
            utils.roomsvisited[19] = 1
        else:
            print("The door is locked.")    

def moveeast():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[12] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            ProgrammingLab.basicDes()
            utils.roomsvisited[12] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[12] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            ProgrammingLab.fancyDes()
            utils.roomsvisited[12] = 1
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
    lst = itemsInhere()
    if obj in lst:
        (utils.inventory).remove(obj)
    else:
        print("Hmm... {} is not in inventory!".format(obj))