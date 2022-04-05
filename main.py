#from Item import Item, Computer
import Item as I
import text as T
import initialize
import os

rooms = []
objects = []
currentroomdict = []

def library(string1, string2):
    inputstring = string1+string2
    inputint = int(inputstring)
    
    currentroomdict.append(inputstring)
    #print(inputstring, inputint, initialize.roomdict[inputint][3], rooms)
    try:
        location = initialize.roomdict[inputint][3]
        rooms.append(location)
        #print(location)
        return location
    except:
        print("Room file not found.")
        return None
 
def whereami(string1, string2):
    inputstring = string1+string2
    inputint = int(inputstring)
    
    location = initialize.roomdict[inputint][0]
    return location
  
def hasItem(obj):
    #Checks objects in the room against string "object"
    import utils
    x = utils.x
    y = utils.y
    where = library(str(x), str(y))
    items = __import__(where).itemshere
    for i in range(len(items)):
        if items[i].name == obj:
            return True
    return False


def processLanguage(obj=None): 
    import utils
    if len(rooms) == 0:
        x = utils.x
        y = utils.y
        library(str(x), str(y))
        import PrivateWorkshop
            
    #basic variables
    validCommand = False
    noun = ""
    verb = ""
    command = input(" ")
    command = command.replace("'.,;:?[]{}|+-*&^%$#@!~_", "")
    splitCommand = command.split()
    
    #Check for non-empty input
    while len(splitCommand) == 0 or not validCommand:
        splitCommand = command.split()
        if len(splitCommand)>0:
          verb = splitCommand[0].lower()
        
        #1-word commands
        if len(splitCommand) == 1: 
            x = utils.x
            y = utils.y
            if (verb == "n") | (verb == "north"):
                where = library(str(x), str(y))
                __import__(where).movenorth()
                validCommand = True
            if (verb == "e") | (verb == "east"):
                where = library(str(x), str(y))
                __import__(where).moveeast()
                validCommand = True
            if (verb == "s") | (verb == "south"):
                where = library(str(x), str(y))
                __import__(where).movesouth()
                validCommand = True
            if (verb == "w") | (verb == "west"):
                where = library(str(x), str(y))
                __import__(where).movewest()
                validCommand = True
            if (verb == "look" and utils.advanced == False):
                where = library(str(x), str(y))
                __import__(where).basicDes()
                validCommand = True
            if (verb == "look" and utils.advanced == True):
                where = library(str(x), str(y))
                __import__(where).fancyDes()
                validCommand = True
            if verb == "help":
                T.help()
                validCommand = True
            if verb == "exit":
                utils.exitgame(currentroomdict)
                validCommand = True
            if verb == "inventory":
                print(utils.inventory)
                validCommand = True
            if verb == "gamemap":
                T.gamemap()
                validCommand = True
            if verb == "cheat":
                utils.cheat = True
                print("Awesome! All doors have been unlocked!")
                validCommand = True
  
        #2-word commands
        if len(splitCommand) >= 2:
            x = utils.x
            y = utils.y
            if command == "where am i":
                locate = whereami(str(x), str(y))
                print("You are currently in", locate, ".")
                validCommand = True
            if command == "game map":
                T.gamemap()
                validCommand = True
            if command == "look again":
                where = library(str(x), str(y))
                __import__(where).fancyDes()
                validCommand = True
            noun = splitCommand[1].lower()
            noun = noun.replace(" ", "")
            if verb == "read":
                if 'userguide'== noun or 'guide' == noun:
                    T.readUserGuide()
                    validCommand = True
                if 'paper' == noun or 'note' == noun:
                    where = library(str(x), str(y))
                    __import__(where).use(noun)
                    validCommand = True
            if (verb == "exam") or (verb == "examine"):
                where = library(str(x), str(y))
                __import__(where).examine(noun)
                validCommand = True
            if (verb == "take"):
                where = library(str(x), str(y))
                __import__(where).take(noun)
                validCommand = True
            if (verb == "use"):
                where = library(str(x), str(y))
                __import__(where).use(noun)
                validCommand = True
            if (verb == "speak to" or verb == "speak with"):
                where = library(str(x), str(y))
                __import__(where).speakTo(noun)
                validCommand = True
            if verb == "read" and ("paper" == noun or "note" == noun):
                where = library(str(x), str(y))
                __import__(where).use(noun)
                validCommand = True
            if ("item" in command or "items" in command) and ("room" in command or "rooms" in command):
                where = library(str(x), str(y))
                __import__(where).listItems()
                validCommand = True
                    
        #3-word commands
        if len(splitCommand) == 3:
            if (verb == "read" or verb == "exam" or verb == "examine"):
                if splitCommand[1].lower() == "users" and splitCommand[2].lower() == "guide":
                    T.readUserGuide()
                    validCommand = True
                if splitCommand[1].lower() == "sticky" and splitCommand[2].lower() == "notes":
                    where = library(str(x), str(y))
                    __import__(where).examine(obj)
                    validCommand = True
        if len(splitCommand) == 0 or not validCommand:
            print("Please input a valid command")
            command = input(" ")
            
while True:
    if os.path.exists('save.py') == True:
        import utils, save
        utils.cheat = save.cheat
        utils.PlayerKey1 = save.PlayerKey1
        utils.advanced = save.advanced
        utils.x = save.x
        utils.y = save.y
        utils.inventory = save.inventory
        utils.roomsvisited = save.visited
        utils.disguise = save.disguise
        utils.programminglabOccupied = save.programminglabOccupied
        os.remove('save.py')

    processLanguage()