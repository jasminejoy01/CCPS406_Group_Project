# -*- coding: utf-8 -*-
"""
Room#4: Outdoors North
"""
import Item as I
import utils
import Greenspace
import OutdoorsMiddle
import CleaningBotStorage

#print("You've stepped outside into the North corridoors.")
#utils.roomsvisited[4] = 1
filename = 'OutdoorsNorth'

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}

def basicDes():
    print("[North Garden Pathway] \n As I exit the building I see many people walking around, all wearing a similar uniform; the crest on their arms reads: 'NASA'. \n There are tall walls that surround the North of the pathway; cameras are stationed on the edges of the walls, facing inside and outside. Logic states that the tall walls surround all the buildings. \n The path to the South streches far; people and other robots can be seen walking in and out of the various buildings. \n The path to the East leads to the door I came from. Above the door reads a sign: 'Housekeeping Storage Bay' \n The path to the West leads to an area filled with benches where people are sitting together in groups. This area looks different compared to the others to the South, but I can't reason why..")

def fancyDes():
    print("[North Garden Pathway] \n There are still many employees walking around the pathway. \n The path stretches south, people and other robots can be seen walking in and out of the various buildings. \n The path to the East leads to [Housekeeping Storage Bay]. \n The path to the West leads to [Outdoor Break Area].")

def movewest():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[10] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            utils.roomsvisited[10] = 1
            Greenspace.basicDes()
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[10] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            utils.roomsvisited[10] = 1
            Greenspace.fancyDes()
        else:
            print("The door is locked.")    

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[5] == 1:
            utils.y = utils.y + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            OutdoorsMiddle.basicDes()
            utils.roomsvisited[5] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[5] == 1:
            utils.y = utils.y + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            OutdoorsMiddle.fancyDes()
            utils.roomsvisited[5] = 1
        else:
            print("The door is locked.")    

def moveeast():    
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[1] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            CleaningBotStorage.basicDes()
            utils.roomsvisited[1] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[1] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            CleaningBotStorage.fancyDes()
            utils.roomsvisited[1] = 1
        else:
            print("The door is locked.") 
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
        (utils.inventory).remove(obj)
    else:
        print("Hmm... {} is not in inventory!".format(obj))