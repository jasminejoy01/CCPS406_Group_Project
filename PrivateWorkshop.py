# -*- coding: utf-8 -*-
"""
Room#1: Private Workshop
"""
import Item as I
import Item2 as I2
import utils
import text as T
import CleaningBotStorage
import os
import room

#print("You're in the Private Workshop.")
filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
computer1 = I.Computer("computer", False, False, "A fairly modern PC. Some sticky notes line the edges of the monitor. A keyboard sits in front of it on the desk.", True, "")
keyboard = I.Item("keyboard", False, False, "A beat up old keyboard. There's a note sitcking out from under it.", True, "A beat up old keyboard. There's a note sitcking out from under it.",)
note = I.Item("note", True, False, "It reads: 'If I forget again: Initials, year of birth, lucky number. No commas or spaces. PS: create a better password.'", True, "It reads: 'If I forget again: Initials Birth year Lucky number, no spaces. PS: create a better password.'")
trash = I.Item("trash", False, False, "Inside the bin, there is a piece of paper.", True, "I could take the paper out of it")
paper = I.Item("paper", False, False, "It reads:\nApril 20, 2020. \nHead of Robotics at NASA, Dr. Cordelia Weaver, has been awarded for remarkable contribution to science for her creation of a highly adaptable cleaning robot. At the age of 28, she is one of the youngest scientists to ever achieve such an acomplishment. We're excited to see what she does next.", True, "It reads:\nApril 20, 2020. \nHead of Robotics at The National Institute for Mechanical Innovation, Cordelia Weaver, has been awarded for remarkable contribution to science for her creation of a highly adaptable cleaning robot. At the age of 28, she is one of the youngest scientists to ever achieve such an acomplishment. We're excited to see what she does next.")
desk = I.Item("desk", False, False, "On the desk sits a computer and keyboard.", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'computer':  [computer1 , None ],
   'keyboard':  [keyboard  , None ],               
   'note':      [note      , None ],
   'trash':     [trash     , None ],
   'paper':     [paper     , None ],
   'terminal':  [terminal1 , None ],
   'desk':      [desk      , None ]
}

def basicDes():
    T.PrivateWorkshop.basicDes()
          
def fancyDes():
    T.PrivateWorkshop.fancyDes()

def movewest():
    if utils.cheat or not terminal1.locked or utils.roomsvisited[1] == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      utils.x = utils.x + 1
      utils.roomsvisited[1] = 1
      if not utils.advanced:
          CleaningBotStorage.basicDes()
      else:
          CleaningBotStorage.fancyDes()
    else:
        print("The door is locked. Use the terminal to leave the room.")      

def movenorth():
    print("Woops! Can't go that way!")

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
