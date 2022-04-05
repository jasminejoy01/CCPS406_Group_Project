# -*- coding: utf-8 -*-
"""
Room#13: The Office of the Head of Contruction Bots.
"""

import Item as I
import Item2 as I2
import utils
import Hallway3
import Puzzle4

#print("You're in the Head of Contruction Office.")
filename = 'ConstructionHeadOffice'
#utils.roomsvisited[13] = 1


## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}

def basicDes():
    print("[Construction Head's Office] \n A spacious room with plenty of locked storage cabinets covering the walls of the room. \n There is a lone desk at the far end of the room with a computer and chair. \n Around the room are different types of storage containers, all containing rolled up sheets of paper. \n One such container is right beside the door; looking at the contents of the paper, it appears to be designed for different types of buildings and rooms. \n To the West is the door that leads back into [Hallway - Section 3]")

def fancyDes():
    print("[Construction Head's Office] \n The Construction Head's Office looks the same as when I had visited earlier. \n Looking around again, there's not much difference compared to when I first came, except it's clear that the Construction Head has a clear love for wooden items. \n His desk is wooden, his shelves are all wooden; it appears that everything in here might have been made by them. \n To the West is [Hallway - Section 3]")

def movewest():
    if utils.constructionChecker == False:
        Puzzle4.constructionchecker()
        utils.constructionChecker == True
        
    if 'ConstructionKeyCard' in utils.inventory.keys():
        I2.Construc_Headoff.item_add()
        
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[19] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            utils.roomsvisited[19] = 1
            Hallway3.basicDes()
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[19] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            utils.roomsvisited[19] = 1
            Hallway3.fancyDes()
        else:
            print("The door is locked.")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")
    #print("You're  moving into Hallway#5.")

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
