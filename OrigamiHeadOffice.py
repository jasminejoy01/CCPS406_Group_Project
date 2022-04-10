# -*- coding: utf-8 -*-
"""
Room#21: Head of Origami Office.
"""
import Item2 as I2
import Item as I
import utils
import Hallway4
#import puzzle6
import text as T
import os
import player

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")
#utils.roomsvisited[21] = 1


## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
origamiKey = I.Item("Dr. Yami's key card", True, False,  "A pristene key card with an elegant origami crane printed onto it.", False, "I'm not sure what to do with this")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'Dr. Yami\'s key card' : [origamiKey, None]
}

def basicDes():
    T.OrigamiHeadOffice.basicDes()
         
def fancyDes():
    T.OrigamiHeadOffice.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    if utils.origamiHeadChecker == False: 
        puzzle6.main()
        utils.origamiHeadChecker = True
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
    utils.roomsvisited[20] = 1
    if not utils.advanced:
      Hallway4.basicDes()
    else:
      Hallway4.fancyDes()

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    lst = itemdictionary.keys()
    #print(obj)
    if obj in lst:
        if itemdictionary[obj][1] == True or itemdictionary[obj][1] == None:
            itemdictionary[obj][0].examine()
    else:
        print("Hmm... {} doesn't seem to be in this room!".format(obj))

def use(obj):
    lst = itemdictionary.keys()
    lst2 = utils.inventory.keys()
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
    if obj in itemdictionary.keys():
        itemdictionary[obj][0].take(filename)
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))
