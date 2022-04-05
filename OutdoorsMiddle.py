# -*- coding: utf-8 -*-
"""
Room#5: Outside space between the storage building and main lab
"""
import Item as I
import utils
import OutdoorsNorth
import OutdoorsSouth
import ConstructionBotStorage
import BuildingEntranceExit

#print("You've stepped into the Middle corridoors outside.")
filename = 'OutdoorsMiddle'
#utils.roomsvisited[5] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
terminal1 = I.Terminal(1)


itemdictionary = { # [Item, isLocked]
  'terminal':  [terminal1 , None ]

}

def basicDes():
    print("[Middle Garden Pathway] \n I'm at the center of the outdoor pathway. \n The path to the North leads towards the building I had booted up from. \n The path to the South leads to the other end of the pathway; it leads to another building. There is a robot holding a broom, it appears they are using it to move debris off the pathway. \n The path to the West leads to an entrance for a much larger building compared to what you've observed. There's an employee sitting at the desk in-between two gates wearing a different uniform compared to the others. Her uniform has the same insignia as the others, but underneath it reads 'SECURITY'. \n The path to the East leads to a building similar to the one I came from. Above the door reads a sign: Construction Storage Bay'")

def fancyDes():
    print("[Middle Garden Pathway] \n I'm at the center of the outdoor pathway. \n The path to the North leads to [North Garden Pathway]. \n The path to the South leads to [South Garden Pathway]. \n The path to the West leads to [Main Facility Entrance]. I see the same guard sitting at the desk in-between two gates. \n The path to the East leads to [Construction Storage Bay]. Looking at the building again, I realize that it has a slightly different look compared to [Housekeeping Storage Bay]; this building has a larger door, and also has other large entrances where supplies are being moved through.")

def movewest():
    if utils.advanced == True:
        utils.x = utils.x + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[11] = 1
        BuildingEntranceExit.basicDes()
    else:
        utils.x = utils.x + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[11] = 1
        BuildingEntranceExit.fancyDes()
  

def movenorth():
    if utils.advanced == True:
        utils.y = utils.y - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[4] = 1
        OutdoorsNorth.basicDes()
    else:
        utils.y = utils.y - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[4] = 1
        OutdoorsNorth.fancyDes()
  

def movesouth():
    if utils.advanced == True:

        utils.y = utils.y + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[6] = 1
        OutdoorsSouth.basicDes()

    else:

        utils.y = utils.y + 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[6] = 1
        OutdoorsSouth.fancyDes()


def moveeast():
    if utils.advanced == True:

        utils.x = utils.x - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[2] = 1
        ConstructionBotStorage.basicDes()

    else:

        utils.x = utils.x - 1
        if utils.x < 0:
            utils.x = 0
        if utils.y < 0:
            utils.y = 0
        utils.roomsvisited[2] = 1
        ConstructionBotStorage.fancyDes()



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