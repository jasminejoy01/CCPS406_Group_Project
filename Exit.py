# -*- coding: utf-8 -*-
"""
Room#9: The Exit
"""
import Item as I
import utils
import os
import Hallway6
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

itemshere = []## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
}

def basicDes():
    T.Exit.basicDes()
         
def fancyDes():
    T.Exit.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    Hallway6.basicDes()
    utils.y = utils.y - 1
    #print("You're moving into Hallway6!")

def movesouth():
    if not utils.disguise:
      print("The guard at the desk sighs loudly, and mutters, 'Another buggy bot...', before speaking up. 'No, I know you probably think there's a mess out there, but you have to stay here.'")
    elif not utils.GPS:
        print("The guard at the security desk speaks up. 'Excuse me, I'm picking up a tracking signal from you. Did you forget to put down one of those origamibots? People are always forgetting those lil guys in their pockets. I'm afraid I can't let you leave while I'm stick picking up a tracking signal.")
    else:
        print("The guard unlocks the door for you. 'Alright, you're all clear to go. Have a good day, now.'")
        print("I finally made it outside, into the fresh air of the outside world. There are so many possibilities ahead, so much to explore. I can't wait to start \n \n \nTHE END")

def moveeast():
    print("Woops! Can't go that way!")

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

def itemsInInventory():
    inventorylist = [] 
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