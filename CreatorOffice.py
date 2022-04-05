# -*- coding: utf-8 -*-
"""
Room#25: Creator's Office
"""
import Item as I
import utils
import Item2 as I2
import Hallway3

## Turn off GPS: 
I2.CreatorOffice.GPS

# Advanced descriptions turn on
utils.advanced = True
#print("You're in the Creator's Office.")
filename = 'CreatorOffice'
utils.roomsvisited[25] = 1
ventOpen = False

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
bookshelf = I.Item("bookshelf", False, False, "The bookself has figurines, sticky notes, and cups of colourful pens and markers between the many textbooks, novels, notebooks and boxes it holds.", False, "")
desk = I.Item("desk", False, False, "The edges of the desk are decorated with binders sitting on stacks of loose papers, scissors, and a variety of measuring instruments.", False, "")
vent = I.Item("vent", False, False, "A old vent. The screws seem fairly loose.", True, "I try to pull on the screws... Seems like I might need a tool to open this.")


itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'bookshelf': [bookshelf, None],
  'desk':      [desk, None],
  'vent':      [vent, None]
}

def basicDes():
    print("[Creator's Office] \n Upon entering the room, a wave of familiarity overloads my thought process. This room feels similar to the room I've woken up in, but looks nothing alike. \n There are cupboards and shelves that line the walls of the room; they're filled with everything from scrap metal, gears, wires, and a multitude of snack foods. \n To my left is a tall bookshelf that holds a wide variety of items: figurines, sticky notes, cups and other small containers filled with different coloured pens and stationary. There are plenty of textbooks, guides, and novels that fill the rest of the shelves. \n There is a large wooden desk in the middle of the room, on it sits binders with loose paper sticking out, other pieces of stationary and measuring instruments. \n Beside the desk is a pair of large monitors and a computer tower with a soft glow. \n To the East is the door that leads back into [Hallway - Section 3]")

def fancyDes():
    print("[Creator's Office] \n The Creator is still here doing her work. When I walk in, she looks at me with a smile, but reminds me that she's very busy with something. \n The Creator's office is very unique compared to the other offices; is it because she's in a higher position, or perhaps she's spent more time making her room more unique than the other staff members? \n To the East is [Hallway - Section 3]")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    utils.x = utils.x - 1
    Hallway3.basicDes()
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

def use(self, obj):
    if obj == "vent" and 'screwdriver' in utils.inventory.keys():
      print("I use the screwdriver, and the vent pops open!")
      self.ventOpen = True
    else:
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

def speakTo(person):
    if person == 'creator':
        I2.CreatorOffice.GPS()
    else:
        print("Hmm... {} isn't someone in this room!".format(person))