# -*- coding: utf-8 -*-
"""
Room#23: The Prototyping Lab"
"""
import Item as I
import utils
import Hallway1
import text as T
import os
import room

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

def fancyDes():
    if not utils.georgeDistracted:
      T.PrototypeWorkshop.fancyDes1()
    else:
      T.PrototypeWorkshop.fancyDes2()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():   
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x - 1
    if not utils.advanced:
        Hallway1.basicDes()
    else:
        Hallway1.fancyDes()

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
 
def take(obj):
  if "key" in obj:
    obj = 'Dr. Ediface\'s key card'
    if utils.georgeDistracted:
      if 2 in utils.PlayerKeys:
        print("I already have the card")
      else:
        itemdictionary['Dr. Ediface\'s key card'][0].take(filename)
        utils.PlayerKeys.append(3)
    else:
      print("I can't do that without being noticed. Maybe I can distract him...")
  else:
    room.take(obj, itemdictionary, filename)
