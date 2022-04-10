# -*- coding: utf-8 -*-
"""
Room#26: Server room
"""
import Item as I
import utils
import Hallway4
import time
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################

itemdictionary = { # [Item, isLocked]
}

def basicDes():
    T.ServerRoom.basicDes()


def fancyDes():
    T.ServerRoom.basicDes()


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
    room.take(obj, itemdictionary, filename)
