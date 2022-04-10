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
#import player

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
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary)
