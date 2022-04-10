# -*- coding: utf-8 -*-
"""
Room#16: The building's side entrance.
"""
import Item as I
import utils
import BotTestingObstacle
import Hallway1
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
machinery = I.Item("machinery", False, False, "Some sort of massive, heavy machinery. It's hard to tell what it does.", True, "")
constructionBot = I.Item("constructionbot", False, False, "A bulky robot, clearly designed for lifting and moving heavy loads. It has a keycard scanner on it.", False, "")


itemdictionary = { # [Item, isLocked]
  'machinery':    [machinery  , None ],
  'constructionbot': [constructionBot, None]
}

def basicDes():
    T.BotTesting.basicDes()
    if utils.blockedDoor:
      print("There's a deactivated constructionBot as well.")
          
def fancyDes():
    T.BotTesting.fancyDes()
    if utils.blockedDoor:
        print("There's a deactivated constructionBot as well.")

def movewest():
  if not utils.blockedDoor:
    utils.x = utils.x + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
        BotTestingObstacle.basicDes()
    else:
        BotTestingObstacle.fancyDes()
  else:
    print("There is a blockage in front of the door.")
  
def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    utils.y = utils.y + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    if not utils.advanced:
      Hallway1.basicDes()
    else:
      Hallway1.fancyDes()

def moveeast():
    print("Woops! Can't go that way!")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
  if "key" in obj or obj == "constructionBot":
    if 3 in utils.PlayerKeys:
      print("I use the Construction keycard to activate the construction bot. It lifts itself up as it awakens, and take a look around the room. \nI point it toward the blockage, and with tremendous strength, the constructionBot pushes the machinery aside.")
      utils.blockedDoor = False
    else:
      print("I don't have the right key for this.")
  else:
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)

