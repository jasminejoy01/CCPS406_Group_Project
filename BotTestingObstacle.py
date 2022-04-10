# -*- coding: utf-8 -*-
"""
Room#22: A lab for testing robots.
"""
import Item as I
import utils
import BotTesting
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
    T.BotTestingObstacleCourse.basicDes()
    if utils.puzzle4 == False:
        Puzzle4.puzzle4()
        utils.puzzle4 = True
         
def fancyDes():
    T.BotTestingObstacleCourse.fancyDes()
    if utils.puzzle4 == False:
        Puzzle4.puzzle4()
        utils.puzzle4 = True
        
def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():  
    utils.x = utils.x - 1
    utils.roomsvisited[16] = 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
      BotTesting.basicDes()   
    else:
      BotTesting.fancyDes()

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
