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
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

itemshere = []## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText


itemdictionary = { # [Item, isLocked]
}

def basicDes():
    T.Exit.basicDes()
    if not utils.blockedDoor:
      print("The constructionBot follows me to the exit.")
         
def fancyDes():
    T.Exit.fancyDes()
    if not utils.blockedDoor:
      print("The constructionBot follows me to the exit.")

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    os.system('cls' if os.name == 'nt' else 'clear')
    Hallway6.basicDes()
    utils.y = utils.y - 1

def movesouth():
    if not utils.disguise:
      print("The guard at the desk sighs loudly, and mutters, 'Another buggy bot...', before speaking up. 'No, I know you probably think there's a mess out there, but you have to stay here.'")
    elif utils.GPS or utils.oriBotGPS:
        print("The guard at the security desk speaks up. 'Excuse me, I'm picking up a tracking signal from you. Did you forget to put down one of those origamibots? People are always forgetting those lil guys in their pockets. I'm afraid I can't let you leave while I'm stick picking up a tracking signal.")
    else:
        print("The guard unlocks the door for you. 'Alright, you're all clear to go. Have a good day, now.'")
        print("I finally made it outside, into the fresh air of the outside world. There are so many possibilities ahead, so much to explore. A whole world await me and my new friends. I can't wait to start \n \n \nTHE END")

def moveeast():
    print("Woops! Can't go that way!")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
