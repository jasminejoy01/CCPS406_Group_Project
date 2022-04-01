# -*- coding: utf-8 -*-
"""
Room#25: Creator's Office
"""
import Item as I
import utils

print("You're in the Creator's Office.")

utils.roomsvisited[25] = 1

## Items in Room
##################

#name, islocked, canTake, inInventory, description, interactable, useText, unlockText
nullItem = I.Item("", False, False, False, "", False, "", "")


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],

}

def basicDes():
    print("There is a door to the East.")

def fancyDes():
    print("A dizzying array of scrap metal, gears, wires, and snack foods lie across the many cupboards that line the room. A tall bookshelf to the left stands with figurines, sticky notes, and cups of colourful pens and markers between the many textbooks, novels, notebooks and boxes it holds. In the middle of the room is a large wooden desk, the edges decorated with binders sitting on stacks of loose papers, scissors, and a variety of measuring instruments. In its center are a pair of large monitors and a softly glowing computer tower.")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    utils.y = utils.y
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving into Hallway#3.")

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

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
    if obj in lst:
        if itemdictionary[obj][1] == True:
            print("It's Locked!")
        else:
            itemdictionary[obj][0].use()
    else:
        print("Hmm... {} can't use an object that's not in this room! You can check your inventory to look for items to use".format(obj))
 
def take(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].take()
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