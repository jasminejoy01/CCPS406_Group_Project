# -*- coding: utf-8 -*-
"""
Room#26: Server room
"""
import Item as I
import Item2 as I2
import utils
import Hallway4
import time
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}

def basicDes():
    T.ServerRoom.basicDes()
    if utils.securityPuzzleCheck == False:
        I2.ServerRoom.smokealarm()

def fancyDes():
    T.ServerRoom.basicDes()
    if utils.securityPuzzleCheck == False:
        I2.ServerRoom.smokealarm()

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
      Hallway4.basicDes() 
    else:
      Hallway4.fancyDes()


def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary)
