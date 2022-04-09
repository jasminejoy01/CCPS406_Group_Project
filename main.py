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

        #Movement
          x = utils.x
          y = utils.y
          where = library(str(x), str(y))
          if "north" in command or verb == "n":
              __import__(where).movenorth()
              validCommand = True
          if "east" in command or verb == "e":
              __import__(where).moveeast()
              validCommand = True
          if "south" in command or verb == "s":
              __import__(where).movesouth()
              validCommand = True
          if "west" in command or verb == "w":
              __import__(where).movewest()
              validCommand = True

        #Player tools
          if "look" in command: #Check if "look at [obj]", else print room des.
            if "at" in command and len(splitCommand)>2:
              if "user" in command:
                    T.readUserGuide()
                    validCommand = True
              else:
                  noun = splitCommand[2]
                  __import__(where).examine(noun)
                  validCommand = True
            else:
              if utils.advanced:
                  __import__(where).fancyDes()
              else:
                  __import__(where).basicDes()

          elif "help" in command:
                  T.help()
                  validCommand = True
          elif "exit" in command:
                  utils.exitgame(currentroomdict)
                  validCommand = True
          elif "inventory" in command or command == "i":
                  items = str(utils.inventory.keys())
                  items = items.replace("'", "")
                  print("I have:",items[11:-2])
                  validCommand = True
          elif "gamemap" in command:
                  T.gamemap()
                  validCommand = True
          elif "cheat" in command:
                  utils.cheat = True
                  print("Awesome! All doors have been unlocked!")
                  validCommand = True
    
          #2-word commands

        #Object interactions
          elif len(splitCommand)>1:
            verb = splitCommand[0]
            noun = splitCommand[1]
            if noun == "bin":
              noun = "trash"
            if verb == "read":
                if "user" in command:
                    T.readUserGuide()
                    validCommand = True
                if 'paper' == noun or 'note' == noun:
                    __import__(where).use(noun)
                    validCommand = True
            elif verb == "exam" or verb == "examine":
                if noun == "user":
                    T.readUserGuide()
                    validCommand = True
                else:
                  __import__(where).examine(noun)
                  validCommand = True
            elif verb == "take" or verb == "get":
                items = str(utils.inventory.keys())
                items = items.replace("'", "")
                items = items[11:-2]
                if noun in items:
                  print(str(utils.inventory.keys()))
                  print("I already have that.")
                else:
                  __import__(where).take(noun)
                validCommand = True
            elif verb == "open" and noun == "vent":
              __import__(where).use(noun)
              validCommand = True
            elif verb == "use":
                validCommand = True
                if "key" in command:
                  if len(utils.PlayerKeys) > 0:
                    print("I have a key. This will let me use a terminal")
                  else:
                    print("I don't have any keys")
                else:
                  __import__(where).use(noun)
              
                #Puzzle 3: sweeping
                if noun == "broom" and x == 3 and y == 1:
                  for i in range(len(utils.PlayerKeys)):
                    if utils.cleanHall:
                      print("'Those things sure do love sweeping...' the guard says to herself.")
                  if not utils.cleanHall:
                    print("The guard carefully inspects my work. 'Well I've certainly seen better, but I suppose it's passable. You may proceed.''")
                    utils.cleanHall = True
                validCommand = True
              
            #if verb == "speak" or verb == "say":
              #This needs a lot of work
             #   where = library(str(x), str(y))
             #   __import__(where).speakTo(noun)
            #    validCommand = True
            if ("item" in command or "items" in command) and ("room" in command or "rooms" in command):
                where = library(str(x), str(y))
                __import__(where).listItems()
                validCommand = True
                    
          if len(splitCommand) == 0 or not validCommand:
            print("Please input a valid command")
            command = input("")
            
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