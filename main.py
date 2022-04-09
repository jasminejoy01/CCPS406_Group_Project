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
        command = command.lower()
        splitCommand = command.split()
        if len(splitCommand)>0:
          verb = splitCommand[0]

        #Helping the user
        if "key" in command:
          if len(utils.PlayerKeys) > 0:
            print("I have a key. This will let me use a terminal")
        
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
            if verb == "inventory" or verb == "i":
                items = str(utils.inventory.keys())
                items = items.replace("'", "")
                print("I have:",items[11:-2])
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
            if command == "look around" and not utils.advanced:
              where = library(str(x), str(y))
              __import__(where).basicDes()
              validCommand = True
            if command == "look around" and utils.advanced:
              where = library(str(x), str(y))
              __import__(where).fancyDes()
              validCommand = True
            if command == "game map":
                T.gamemap()
                validCommand = True
            if "north" in command:
                where = library(str(x), str(y))
                __import__(where).movenorth()
                validCommand = True
            if "east" in command:
                where = library(str(x), str(y))
                __import__(where).moveeast()
                validCommand = True
            if "south" in command:
                where = library(str(x), str(y))
                __import__(where).movesouth()
                validCommand = True
            if "west" in command:
                where = library(str(x), str(y))
                __import__(where).movewest()
                validCommand = True
            if command == "look again":
                where = library(str(x), str(y))
                __import__(where).fancyDes()
                validCommand = True

            #object interactions
            noun = splitCommand[1]
            noun = noun.replace(" ", "")
            if noun == "bin":
              noun = "trash"
            where = library(str(x), str(y))
            if verb == "read":
                if "user" in command:
                    T.readUserGuide()
                    validCommand = True
                if 'paper' == noun or 'note' == noun:
                    __import__(where).use(noun)
                    validCommand = True
            elif (verb == "exam") or (verb == "examine"):
                __import__(where).examine(noun)
                validCommand = True
            elif (verb == "take" or verb == "get"):
                __import__(where).take(noun)
                validCommand = True
            elif (verb == "open") and noun == "vent":
              __import__(where).use(noun)
              validCommand = True
            elif (verb == "use") and noun != "key":
                __import__(where).use(noun)
              
                #Puzzle 3: sweeping
                if noun == "broom" and x == 3 and y == 1:
                  hasKey2 = False
                  for i in range(len(utils.PlayerKeys)):
                    if utils.PlayerKeys[i] == 2:
                      hasKey2 = True
                      print("'Those things sure do love sweeping...' the guard says to herself.")
                  if not hasKey2:
                    print("The guard carefully inspects my work. 'Well I've certainly seen better, but I suppose it's passable. You may proceed.''")
                    utils.PlayerKeys.append(2)
                validCommand = True
              
            if (verb == "speak to" or verb == "speak with"):
                where = library(str(x), str(y))
                __import__(where).speakTo(noun)
                validCommand = True
            if ("item" in command or "items" in command) and ("room" in command or "rooms" in command):
                where = library(str(x), str(y))
                __import__(where).listItems()
                validCommand = True
                    
        #3-word commands
        if len(splitCommand) >= 3 and not validCommand:
            if (verb == "read" or verb == "exam" or verb == "examine"):
                if "user" in splitCommand[1]:
                    T.readUserGuide()
                    validCommand = True
                if splitCommand[1] == "sticky" and splitCommand[2] == "notes":
                    where = library(str(x), str(y))
                    __import__(where).examine(obj)
                    validCommand = True
            if (splitCommand[0] == "look"):
              if "user" in command:
                    T.readUserGuide()
                    validCommand = True
              else:
                noun = splitCommand[1]
                noun = noun.replace(" ", "")
                where = library(str(x), str(y))
                __import__(where).use(noun)
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