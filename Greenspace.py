# -*- coding: utf-8 -*-
"""
Room#10: Greenspace break area
"""
import Item as I
import utils
import OutdoorsNorth

filename = 'Greenspace'
utils.roomsvisited[10] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}


def basicDes():
    print("[Outdoor Break Area] \n I'm surrounded by many employees, walking to and from different benches, tables, and areas. \n Upon closer inspection, it's clear that this area has a lot more foliage compared to the rest of the pathway. There are significantly more sections of shrubbery and plants, along with rows of large trees providing shade for the people below. \n The path to the East leads back to [North Garden Pathway].")

def fancyDes():
    print("[Outdoor Break Area] \n There are still many employees working outdoors. They're all wearing similar uniforms, but I notice now that each employee has their own accessories. Some have different colored/branded lanyards, others have a combination of pins, buttons, earrings, and other jewelry that seem to make each person more unique. \n The abundance of trees and flowers out here are amazing; they're all varying colors and designs, and the trees that offer shade for everyone, also are host to different small animals and fruits. The colors and beauty of the foliage have to be the main attraction of this space. \n The path to the East leads back to [North Garden Pathway].")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[4] == 1:
            utils.x = utils.x - 1
            OutdoorsNorth.basicDes()
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[4] == 1:
            utils.x = utils.x - 1
            OutdoorsNorth.fancyDes()
        else:
            print("The door is locked.")    
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving back to Outdoors (North)!", utils.x, utils.y)

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