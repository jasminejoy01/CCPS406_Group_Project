# -*- coding: utf-8 -*-
"""
Room#2: Storage for Construction Bots
"""

import Item as I
import utils
import OutdoorsMiddle
#import Puzzle4
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText

itemdictionary = { # [Item, isLocked]    
}

def basicDes():
    T.ConstructionBotStorage.basicDes()
         
def fancyDes():
    T.ConstructionBotStorage.fancyDes()

def movewest():
#    if utils.constructionBotChecker == False:
#        Puzzle4.consbot()
#        utils.constructionBotChecker == True
    utils.x = utils.x + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.roomsvisited[5] = 1    
    if not utils.advanced:
      OutdoorsMiddle.basicDes()
    else:
      OutdoorsMiddle.fancyDes()  


def movenorth():
    print("Woops! Can't go that way!")

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
