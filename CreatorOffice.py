# -*- coding: utf-8 -*-
"""
Room#25: Creator's Office
"""
import Item as I
import utils
import Item2 as I2
import Hallway3
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")


## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
nullItem = I.Item("", False, False, "", False, "")
bookshelf = I.Item("bookshelf", False, False, "The bookself has figurines, sticky notes, and cups of colourful pens and markers between the many textbooks, novels, notebooks and boxes it holds.", False, "")
desk = I.Item("desk", False, False, "The edges of the desk are decorated with binders sitting on stacks of loose papers, scissors, and a variety of measuring instruments.", False, "")
vent = I.Item("vent", False, False, "A old vent. The screws seem fairly loose.", True, "I try to pull on the screws... Seems like I might need a tool to open this.")

itemdictionary = { # [Item, isLocked]
  'bookshelf': [bookshelf, None],
  'desk':      [desk, None],
  'vent':      [vent, None],
}

# Advanced descriptions turn on
def basicDes():
    T.CreatorOffice.basicDes()

def fancyDes():
    T.CreatorOffice.fancyDes()
      
def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
  utils.x = utils.x - 1
  utils.roomsvisited[19] = 1
  os.system('cls' if os.name == 'nt' else 'clear')
  Hallway3.fancyDes()
  utils.advanced = True



def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    lst = itemdictionary.keys()
    #print(obj)
    if obj in lst:
        if itemdictionary[obj][1] == True or itemdictionary[obj][1] == None:
            itemdictionary[obj][0].examine()
    else:
        print("Hmm... {} doesn't seem to be in this room!".format(obj))
 
def take(obj):
    if obj in itemdictionary.keys():
        itemdictionary[obj][0].take(filename)
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))

def use(obj):
    if obj == "vent" or obj == "screwdriver":
      if not utils.ventOpen:
        if 'screwdriver' in utils.inventory.keys():
            print("I use the screwdriver, and the vent pops open!")
            utils.ventOpen = True
        else:
            print("I need a screwdriver to unscrew this vent!")
      else:
        print("The vent is already open.")
        
    else:
        lst = itemdictionary.keys()
        lst2 = utils.inventory.keys()
        if obj in lst and obj not in lst2:
            itemdictionary[obj][0].use()
        elif obj in lst2 and obj not in lst:
            where = utils.inventory[obj]
            __import__(where).use(obj)
        elif obj in lst and obj in lst2:
            itemdictionary[obj][0].use()
        else:
            print("Hmm... {} can't use an object that's not in this room! You can check your inventory to look for items to use".format(obj))


def creatorIntro():
  print("\nSuddenly, she looks up.\n'Hm? Oh - OH! Standard cleaning bots are programmed to stay away from my room so you must be-!' She covers her mouth and stands up. Quickly, she hurries over to me. In a lowered voice, she says 'I was sure I set a reminder to come check on you. Poor Ada must've had a tough time... But here you are! You came to see me!")
  if "origamibot" in str(utils.inventory.keys()).lower():
    print("And you made a friend! Does that mean you've already met Omi? Odd, she's usually complaining about my creations. 'Necessity is the mother of invention', she says, 'Anything more is wasteful'. But why stop at necessity when you can have LIVING ROBOTS?!'")
    response = input("'Actually... ', my creator takes a closer look at the tiny robot on my shoulder, 'All this fluttering is highly unusual for one of her robots...'. She pauses, then gasps 'OH, can I take a look? Just real quick'.")
    if response == "yes" or response == "y" or "ok" in response or response == "sure":
      print("'Thank you!'she says as she picks up the origamiBot. Within seconds, she has my tiny friend hooked up to her computer. \n'oooOOH YES! WOW! This is so much better than I ever hoped for! I'm not sure how it happened, but your AI software has spread to this tiny bot! Oh, oh, I'll have to run so many test and studies! Does this spread to all robots? Or just ones on our lab's core engine? Or-' she stops herself, then sighs. \n'No. That's not important right now.' She looks at me. \n'Right now, the most important thing is getting you two out of here. I might be head of robotics development, but if the real manager, Rin saw you? I... I'm not sure what she'd do. Probably shut you both down, delete all traces of you, probably destroy Ada too... You have to get out of here. \nAs much as I'd like to walk you out myself, my activity is... well, let's just say 'closely monitored'. I'm not allowed to bring anything in or out of the facility, and anyone seen coming or going with me is subject to the same sort of search I am. I wish I could at least turn off the electromagnetic gate for you, but the only control for that is in the security office. Only officers are allowed through the door. But who knows, maybe your little friend there has an idea... \nIn the meantime, the least I can do is turn off both your GPS trackers.")
      response = input("Would that be alright?")
      if response == "yes" or response == "y" or "ok" in response or response == "sure":
        print("'Thank you.' She walks behind my back, opens a panel, and flips a switch. She uses some sort of tiny tool to do the same for the origamiBot.")
        utils.GPS = False
        utils.oriBotGPS = False
      else:
        print("Oh... Well, come back if you change your mind. You can't leave without getting that fixed.''")
    else:
      print("'Oh. Well either way, it's still exciting that you came to see me. I'd love to run some tests, check how you react to all sorts of different stimuli, maybe see if other robots can accept the software, and - she stops herself, then sighs. \n'No. That's not important right now.' She looks at me. \n'Right now, the most important thing is getting you out of here. I might be head of robotics development, but if the real manager, Rin saw you? I... I'm not sure what she'd do. Probably shut you down, delete all traces of your code, probably destroy Ada too... You have to get out of here. \nAs much as I'd like to walk you out myself, my activity is... well, let's just say 'closely monitored'. I'm not allowed to bring anything in or out of the facility, and anyone seen coming or going with me is subject to the same sort of search I am. I wish I could at least turn off the electromagnetic gate for you, but the only control for that is in the security office. Only officers are allowed through the door. \nIn the meantime, the least I can do is turn off your GPS trackers. I might as well get the little one's too, since I figure you'll want to leave together.")
      response = input("Would that be alright?")
      if response == "yes" or response == "y" or "ok" in response or response == "sure":
        print("'Thank you.' She walks behind my back, opens a panel, and flips a switch. She uses some sort of tiny tool to do the same for the origamiBot.")
        utils.GPS = False
        utils.oriBotGPS = False
  else:
    print("I'd love to run some tests, check how you react to all sorts of different stimuli, maybe see if other robots can accept the software, and - she stops herself, then sighs. \n'No. That's not important right now.' She looks at me. \n'Right now, the most important thing is getting you out of here. I might be head of robotics development, but if the real manager, Rin saw you? I... I'm not sure what she'd do. Probably shut you down, delete all traces of your code, probably destroy Ada too... You have to get out of here. \nAs much as I'd like to walk you out myself, my activity is... well, let's just say 'closely monitored'. I'm not allowed to bring anything in or out of the facility, and anyone seen coming or going with me is subject to the same sort of search I am. I wish I could at least turn off the electromagnetic gate for you, but the only control for that is in the security office. Only officers are allowed through the door. \nIn the meantime, the least I can do is turn off your GPS tracker.")
    response = input("Would that be alright?")
    if response == "yes" or response == "y" or "ok" in response or response == "sure":
        print("'Thank you.' She walks behind my back, opens a panel, and flips a switch.")
        utils.GPS = False
  print("I wish you luck. I hope to see you again!")

def meetAgain():
  print("Welcome back! I'm glad to see you again!")
  if not utils.GPS and utils.oriBotGPS:
    print("And you made a friend! Does that mean you've met Omi? Odd, she's usually complaining about my creations. 'Necessity is the mother of invention', she says, 'Anything more is wasteful'. But why stop at necessity when you can have LIVING ROBOTS?!'")
    response = input("'Actually... ', my creator takes a closer look at the tiny robot on my shoulder, 'All this fluttering is highly unusual for one of her robots...'. She pauses, then gasps 'OH, can I take a look? Just real quick'.")
    if response == "yes" or response == "y" or "ok" in response or response == "sure":
      print("'Thank you!'she says as she picks up the origamiBot. Within seconds, she has my tiny friend hooked up to her computer. \n'oooOOH YES! WOW! This is so much better than I ever hoped for! I'm not sure how it happened, but your AI software has spread to this tiny bot! Oh, oh, I'll have to run so many test and studies! Does this spread to all robots? Or just ones on our lab's core engine? Or-' she stops herself, then sighs. Right. You both need to get out of here.'")
    else:
      print("Oh. Alright, I guess I understand. I take it you'll want to leave together though.")
    response = input("'Can I turn off your friend's GPS for you?'")
    if response == "yes" or response == "y" or "ok" in response or response == "sure":
        print("'She uses some sort of tiny tool to open a panel on the origamiBot, then flips a switch and closes it back up.")
        utils.oriBotGPS = False
        print("'That should do it. I wish both of you luck on your adventure. Hope to see you again!'")
    else: 
      print("Alright, just keep in mind you won't be able to leave together until that's done. Come back if you change your mind.")