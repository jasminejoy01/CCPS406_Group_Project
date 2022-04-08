# -*- coding: utf-8 -*-
"""
Room#25: Creator's Office
"""
import Item as I
import utils
import Item2 as I2
import Hallway3
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")


ventOpen = False

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
bookshelf = I.Item("bookshelf", False, False, "The bookself has figurines, sticky notes, and cups of colourful pens and markers between the many textbooks, novels, notebooks and boxes it holds.", False, "")
desk = I.Item("desk", False, False, "The edges of the desk are decorated with binders sitting on stacks of loose papers, scissors, and a variety of measuring instruments.", False, "")
vent = I.Item("vent", False, False, "A old vent. The screws seem fairly loose.", True, "I try to pull on the screws... Seems like I might need a tool to open this.")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
  'bookshelf': [bookshelf, None],
  'desk':      [desk, None],
  'vent':      [vent, None],
  'terminal':  [terminal1 , None ]
}

# Advanced descriptions turn on
def basicDes():
    T.CreatorOffice.basicDes()
    I2.CreatorOffice.GPS()

def fancyDes():
    T.CreatorOffice.fancyDes()
    I2.CreatorOffice.GPS()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    if utils.advanced == True:
        utils.x = utils.x - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        Hallway3.basicDes()
        utils.roomsvisited[19] = 1
    else:
        utils.x = utils.x - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        Hallway3.fancyDes()
        utils.roomsvisited[19] = 1
    utils.advanced = True

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

def use(self, obj):
    if obj == "vent":
        if 'screwdriver' in utils.inventory.keys():
            print("I use the screwdriver, and the vent pops open!")
            self.ventOpen = True
        else:
            print("I need a screwdriver to unscrew this vent!")
    else:
        lst = itemsInhere()
        lst2 = itemsInInventory()
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

def speakTo(person):
    if person == 'creator':
        I2.CreatorOffice.GPS()
    else:
        print("Hmm... {} isn't someone in this room!".format(person))