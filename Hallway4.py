# -*- coding: utf-8 -*-
"""
Room#20: Hallway 4
"""
import Item as I
import utils
import Server
import OrigamiHeadOffice
import Hallway5
import Hallway3

#print("You're in the Hallway#4.")
filename = 'Hallway4'
#utils.roomsvisited[20] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'terminal':  [terminal1     , None ]    
}


def basicDes():
    print("[Hallway – Section 4] \n I've reached the corner for this hallway, written on the floor is '#4'. \n To the North is [Hallway – Section #3]. \n To the South is a door with a sign that reads: \n 'Head of Abstract Solutions \n Ori Yami'. \n To the West is a door that reads: \n 'Server Room'. \n To the East, I see the hallway extending. There are more doors along the hallway, and it appears that the hallway turns another time to the right.")

def fancyDes():
    print(" [Hallway - Section 4] \n I've reached the corner for this hallway, written on the floor is '#4'. \n To the North is [Hallway – Section #3]. \n To the South is [Head of Abstract Solutions]. \n To the West is [Server Room]. \n To the East is [Hallway - Section 5].")

def movewest():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[26] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Server.basicDes()
            utils.roomsvisited[26] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[26] == 1:
            utils.x = utils.x + 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Server.fancyDes()
            utils.roomsvisited[26] = 1
        else:
            print("The door is locked.")

def movenorth():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[19] == 1:
            utils.y = utils.y - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway3.basicDes()
            utils.roomsvisited[19] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[19] == 1:
            utils.y = utils.y - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway3.fancyDes()
            utils.roomsvisited[19] = 1
        else:
            print("The door is locked.")    

def movesouth():
    oriUnlocked = False  
    for i in range(len(utils.PlayerKeys)):
      if utils.PlayerKeys[i] == 4:
        oriUnlocked = True
    if not oriUnlocked and not utils.cheat:
      print("I try to open a door marked 'Head of Origami Bots', but it's locked. It sounds like there's someone inside.")
    else: 
        if utils.advanced == True:
            if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[21] == 1:
                utils.y = utils.y + 1
                if utils.x < 0:
                    utils.x = 0
                if utils.y < 0:
                    utils.y = 0
                OrigamiHeadOffice.basicDes()
                utils.roomsvisited[21] = 1
            else:
                print("The door is locked.")
        else:
            if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[21] == 1:
                utils.y = utils.y + 1
                if utils.x < 0:
                    utils.x = 0
                if utils.y < 0:
                    utils.y = 0
                OrigamiHeadOffice.fancyDes()
                utils.roomsvisited[21] = 1
            else:
                print("The door is locked.")    

def moveeast():
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[14] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway5.basicDes()
            utils.roomsvisited[14] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[14] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway5.fancyDes()
            utils.roomsvisited[14] = 1
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