# -*- coding: utf-8 -*-
"""
Room#6: Outside space between the storage building and main lab
"""
import Item as I
import utils
import OrigamiBotStorage
import OutdoorsMiddle

#print("You've stepped into the South corridoors outside.")
filename = 'OutdoorsSouth'
utils.roomsvisited[6] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'terminal':  [terminal1     , None ]    
}

def basicDes():
    print("[South Garden Pathway] \n I'm at the southmost part of the pathway. \n The path to the North leads up to the Middle Garden Pathway. \n The path to the East leads to another building, similar to the previous two, but unique? Above the door reads a sign: 'Abstract Solutions Storage Bay' \n The robot holding the broom is still removing the debris off the pathway. They carry the NASA insignia on their arm, and on their chest reads a number: ''#11'.")

def fancyDes():
    print("[South Garden Pathway] \n I'm at the southmost part of the pathway. \n The path to the North leads to [Middle Garden Pathway]. \n The path to the East leads to [Abstract Solutions Storage Bay]. \n The robot holding the broom has since finished their task, and has moved on to wiping the windows of the Abstract Solutions Storage Bay. \n Observing this building again, I notice that it has a completely different look compared to the other two storage bays. The walls twist and turn differently, nothing at all like the plain, straight walls that protect the other storage bays.")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[5] == 1:
            utils.y = utils.y - 1
            OutdoorsMiddle.basicDes()
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[5] == 1:
            utils.y = utils.y - 1
            OutdoorsMiddle.fancyDes()
        else:
            print("The door is locked.")    
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[3] == 1:
            utils.x = utils.x - 1
            OrigamiBotStorage.basicDes()
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[3] == 1:
            utils.x = utils.x - 1
            OrigamiBotStorage.fancyDes()
        else:
            print("The door is locked.")    
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0

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