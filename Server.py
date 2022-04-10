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
  if "panel" in obj or "control" in obj or "electrical" in obj:
    print("The panel labels controls for everything from lights to emergency alarms in every room. Not locks, unfortunately. I could probably use this for something else.")
  else:
    room.examine(obj, itemdictionary)

def use(obj):
  if "panel" in obj or "wire" in obj or "copper" in obj or "control" in obj or "electrical" in obj:
    if utils.inInventory("wire"):
      print("I push my copper wire into the electrical panel, and sparks fly.")
      print("I hear an alarm go off down the hall, and people complaining as they move out.")
    elif "panel" in obj or "control" in obj or "electrical" in obj:
      print("I could probably use something to short-circuit this.")
    else:
      room.use(obj, itemdictionary)
  else:
    room.use(obj, itemdictionary)

 
def take(obj):
    room.take(obj, itemdictionary, filename)
