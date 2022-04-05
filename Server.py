# -*- coding: utf-8 -*-
"""
Room#26: Server room
"""
import Item as I
import Item2 as I2
import utils
import Hallway4
import time

#print("You're in the Server room.")
filename = 'Server'
#utils.roomsvisited[26] = 1

## Items in Room
##################

terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
   'terminal':  [terminal1 , None ]
}

def basicDes():
    print("[Server Room] \n There is nothing in this room except many large glass boxes, all containing flashing lights, and wires pouring in and out of the shelves of lights. \n One thing to note of this room is the amount of ventilation that's been designed; I reason that these large glass boxes must create a large amount of heat. \n To the East is the door that leads back into [Hallway - Section 4]")
    if utils.securityPuzzleCheck == False:
        I2.ServerRoom.smokealarm()

def fancyDes():
    print("[Server Room] \n The most boring room in the building; bland, colorless (minus the blinking red and green lights), and uninteresting. \n There are ribbons hanging from the vents above the room; they're flying in rythym to the air current. \n To the East is the door that leads back into [Hallway - Section 4] \n  I see a panel I haven't noticed before; There's a wire labeled Smoke Alarm.")
    if utils.securityPuzzleCheck == False:
        I2.ServerRoom.smokealarm()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[20] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway4.basicDes()
            utils.roomsvisited[20] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[20] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway4.fancyDes()
            utils.roomsvisited[20] = 1
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