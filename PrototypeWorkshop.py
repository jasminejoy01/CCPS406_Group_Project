# -*- coding: utf-8 -*-
"""
Room#23: The Prototyping Lab"
"""
import Item as I
import Item2 as I2
import utils
import Hallway1
#import Puzzle4
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
jacket = I.Item("jacket", False, False, "Some sort of lab coat. I can see a keycard in its pocket.", False, "")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
    'wire':       [wire  , None],
    'Dr. Ediface\'s key card' : [constructionKey, None],
    'jacket':     [jacket, None]
}

def basicDes():
    if not utils.georgeDistracted:
      T.PrototypeWorkshop.basicDes1()
    else:
      T.PrototypeWorkshop.basicDes2()
#    if utils.prototypeChecker == False: # and utils.roomsvisited[23] == 1:
#        Puzzle4.breakbotcheck()
#        utils.prototypeChecker == True

def fancyDes():
    if not utils.georgeDistracted:
      T.PrototypeWorkshop.fancyDes1()
    else:
      T.PrototypeWorkshop.fancyDes2()
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
  if "key" in obj:
    obj = 'Dr. Ediface\'s key card'
    if utils.georgeDistracted:
      if 2 in utils.PlayerKeys:
        print("I already have the card")
      else:
        itemdictionary['Dr. Ediface\'s key card'][0].take(filename)
        utils.PlayerKeys.append(2)
    else:
      print("I can't do that without being noticed. Maybe I can distract him...")
  else:
    lst = itemsInhere()
    if obj == "copperwire":
        obj = "wire"
    if obj in lst:
        print(obj, itemdictionary[obj][0].canTake)
        if itemdictionary[obj][0].canTake:
          itemdictionary[obj][0].take(filename)
        else:
          print("I can't take that.")
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))
