# -*- coding: utf-8 -*-
"""
Room#23: The Prototyping Lab"
"""
import Item as I
import Item2 as I2
import utils
import Hallway1

#print("You're in the Prototyping Lab.")
filename = 'PrototypeWorkshop'
#utils.roomsvisited[23] = 1

if utils.prototypeChecker == False and utils.roomsvisited[23] == 1:
    import Puzzle4
    Puzzle4.breakbotcheck()
    utils.prototypeChecker == True


## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
wire = I.Item("wire", False, False, "A piece of copper wire, highly conductive", False, "I push the copper wire into the pannel")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
    'wire':       [wire  , None],
    'terminal':  [terminal1 , None ]
}

def basicDes():
    print("[Prototype Workshop]\nThis room is very cluttered; there are gears and bits of wire scattered everywhere on the floor, in storage containers, and on the tables.\nThe robots in this room look like they're a mixture of the other models I've seen on the compound.\nOn one of the tables near the door is one of the more complete looking robots, there are papers beside it that read 'Construction 1.6 Prototype'; it looks fairly fragile in this state.\nTo the East is the door that leads back into [Hallway - Section 1]")

def fancyDes():
    print("[Prototype Workshop]\nThis room is still filled with many colorful spare parts and tools.\nThe bins have a dizzying array of different colored wires, printing material, and spare parts.\nI only notice now the 'Construction 1.6 Prototype' is made up of mismatched coloured parts.\nTo the East is [Hallway - Section 1]")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():   
    if utils.advanced == True:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[17] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway1.basicDes()
            utils.roomsvisited[17] = 1
        else:
            print("The door is locked.")
    else:
        if utils.cheat == True or terminal1.locked == False or utils.roomsvisited[17] == 1:
            utils.x = utils.x - 1
            if utils.x < 0:
                utils.x = 0
            if utils.y < 0:
                utils.y = 0
            Hallway1.fancyDes()
            utils.roomsvisited[17] = 1
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
          if obj == "copperwire":
            I2.PrototypeWorkshop.item_add()
          else:
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