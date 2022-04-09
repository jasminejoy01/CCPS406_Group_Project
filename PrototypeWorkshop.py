# -*- coding: utf-8 -*-
"""
Room#23: The Prototyping Lab"
"""
import Item as I
import Item2 as I2
import utils
import Hallway1
import Puzzle4
import text as T
import os
import player

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
wire = I.Item("wire", False, False, "A piece of copper wire, highly conductive", False, "I push the copper wire into the pannel")
constructionKey = I.Item("Dr. Ediface's key card", True, False,  "A well-worn key card. It doesn't look like much.", False, "I'm not sure what to do with this")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
    'wire':       [wire  , None],
    'Dr. Ediface\'s key card' : [constructionKey, None]
}

def basicDes():
    T.PrototypeWorkshop.basicDes()
    if utils.prototypeChecker == False: # and utils.roomsvisited[23] == 1:
        Puzzle4.breakbotcheck()
        utils.prototypeChecker == True

def fancyDes():
    T.PrototypeWorkshop.fancyDes()
    if utils.prototypeChecker == False: # and utils.roomsvisited[23] == 1:
        Puzzle4.breakbotcheck()
        utils.prototypeChecker == True

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():   
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    utils.roomsvisited[17] = 1
    if not utils.advanced:
        Hallway1.basicDes()
    else:
        Hallway1.fancyDes()

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
  if obj == "key":
      itemdictionary['Dr. Ediface\'s key card'][0].take(filename)
      utils.PlayerKeys.append(2)
  else:
    lst = itemsInhere()
    if obj in lst:
          if obj == "copperwire":
            I2.PrototypeWorkshop.item_add()
          else:
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