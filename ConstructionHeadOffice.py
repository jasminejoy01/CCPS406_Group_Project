# -*- coding: utf-8 -*-
"""
Room#13: The Office of the Head of Contruction Bots.
"""

import Item as I
import Item2 as I2
import utils
import Hallway3
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
    T.ConstructionHeadOffice.basicDes()
         
def fancyDes():
    T.ConstructionHeadOffice.fancyDes()

def movewest():
    if utils.constructionChecker == False:
        Puzzle4.constructionchecker()
        utils.constructionChecker = True
    utils.x = utils.x + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.roomsvisited[19] = 1        
    if not utils.advanced:
      Hallway3.basicDes()
    else:
      Hallway3.fancyDes()

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")
    #print("You're  moving into Hallway#5.")

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
