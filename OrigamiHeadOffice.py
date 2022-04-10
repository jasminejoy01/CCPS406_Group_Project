# -*- coding: utf-8 -*-
"""
Room#21: Head of Origami Office.
"""
import Item as I
import utils
import Hallway4
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
origamiKey = I.Item("Dr. Yami's key card", True, False,  "A pristene key card with an elegant origami crane printed onto it.", False, "I'm not sure what to do with this")
desk = I.Item("desk", False, False, "An elegane desk with crisp, clean edges. It has a single drawer.", False, "")
drawer = I.Item("desk", True, False, "A drawer with a minimalist rectangular knob.", True, "I open the drawer. In it is a keycard with an origami crane printed onto it.")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'Dr. Yami\'s key card' : [origamiKey, None],
  'desk' :                 [desk, None],
  'drawer' :               [drawer, None]
}

def basicDes():
    T.OrigamiHeadOffice.basicDes()
         
def fancyDes():
    T.OrigamiHeadOffice.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y - 1
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
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
  if "key" in obj:
      obj = 'Dr. Yami\'s key card'
      if utils.inInventory(obj):
        print("I already have the card")
      else:
        itemdictionary['Dr. Yami\'s key card'][0].take(filename)
        utils.PlayerKeys.append(2)
  else:
    room.take(obj, itemdictionary, filename)
