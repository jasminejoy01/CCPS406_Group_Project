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
    if not utils.advanced:
        if utils.cheat or terminal1.locked == False or utils.roomsvisited[1] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            utils.roomsvisited[1] = 1
            CleaningBotStorage.basicDes()
        else:
            print("The door is locked. Use the terminal to leave the room.")
    else:
        if utils.cheat or terminal1.locked == False or utils.roomsvisited[1] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            CleaningBotStorage.fancyDes()
            utils.roomsvisited[1] = 1
        else:
            print("The door is locked. Use the terminal to leave the room.")      

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

def itemsInInventory():
    inventorylist = []
    if len(utils.inventory) == 0 : 
        return inventorylist
    else:
        for each in utils.inventory.keys():
            inventorylist.append(each)
        return inventorylist

def listItems():
    lst = itemsInhere()
    for each in lst:
        print(each)
    
def examine(obj):
    lst = itemsInhere()
    #print(obj)
    if obj in lst:
        if itemdictionary[obj][1] == True or itemdictionary[obj][1] == None:
            itemdictionary[obj][0].examine()
    else:
        print("Hmm... {} doesn't seem to be in this room!".format(obj))

def use(obj):
    lst = itemsInhere()
    lst2 = itemsInInventory()
    #print(obj in lst, obj in lst2)
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
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].take(filename)
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))

def unlock(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].unlock()
    else:
        print("Hmm... {} cannot be unlocked!".format(obj))

def removeInventory(obj):
    lst = itemsInhere()
    if obj in lst:
        (utils.inventory).drop(obj)
    else:
        print("Hmm... {} is not in inventory!".format(obj))