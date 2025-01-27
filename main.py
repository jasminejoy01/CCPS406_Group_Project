#from Item import Item, Computer
import Item as I
import text as T
import initialize
import os

rooms = []
objects = []

def library(string1, string2):
    import utils
    inputstring = string1+string2
    inputint = int(inputstring)
    
    (utils.roomlist).append(inputstring)
    #utils.roomlist = currentroomdict
    #print(inputstring, inputint, initialize.roomdict[inputint][3], rooms)
    try:
        location = initialize.roomdict[inputint][3]
        rooms.append(location)
        return location
    except:
        print("Room file not found.")
        return None
 
def whereami(string1, string2):
    inputstring = string1+string2
    inputint = int(inputstring)
    #print(inputint)
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
    #print(utils.roomlist)
    import utils
    if len(utils.roomlist) == 0:
        T.intro()
        x = utils.x
        y = utils.y
        library(str(x), str(y))
        import PrivateWorkshop
        #T.intro()
            
    #basic variables
    validCommand = False
    noun = ""
    verb = ""
    command = input(" ")
    command = command.replace("'.,;:?[]{}|+-*&^%$#@!~_", "")
    splitCommand = command.split()
    
    #Check for non-empty input
    while len(splitCommand) == 0 or validCommand == False:
        command = command.lower()
        splitCommand = command.split()
        if len(splitCommand)>0:
          verb = splitCommand[0]

        #Movement
          x = utils.x
          y = utils.y
          where = library(str(x), str(y))
          if "where am i" in command or "whereami" in command:
              print("You're in",whereami(str(x), str(y)))
              validCommand = True
          if "north" in command or verb == "n":
              __import__(where).movenorth()
              validCommand = True
          elif "east" in command or verb == "e":
              __import__(where).moveeast()
              validCommand = True
          elif "south" in command or verb == "s":
              __import__(where).movesouth()
              validCommand = True
          elif "west" in command or verb == "w":
              __import__(where).movewest()
              validCommand = True

        #Player tools
          elif "look" in command: #Check if "look at [obj]", else print room des.
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
                  validCommand = True
              else:
                  __import__(where).basicDes()
                  validCommand = True

          elif "help" in command:
                  T.help()
                  validCommand = True
          elif "exit" in command:
                  utils.exitgame()
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
            if "copper wire" in command:
              noun = "wire"
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
                if utils.inInventory(noun) and not "key" in command:
                  print("I already have that.")
                else:
                  __import__(where).take(noun)
                validCommand = True
            elif verb == "open" and noun == "vent":
              __import__(where).use(noun)
              validCommand = True
            elif verb == "wear" and (noun == "hat" or noun == "coat") and x == 2 and y == 3:
              __import__(where).use(noun)
              utils.disguise = True
              validCommand = True
            elif verb == "use":
                validCommand = True
                #if "key" in command:
                #  if len(utils.PlayerKeys) > 0:
                #    print("I have a key. This will let me use a terminal")
                #  else:
                #    print("I don't have any keys")
                #else:
                __import__(where).use(noun)
              
                #Puzzle 3: sweeping
                if noun == "broom" and x == 3 and y == 1:
                  for i in range(len(utils.PlayerKeys)):
                    if utils.cleanHall:
                      print("'Those things sure do love sweeping...' the guard says to herself.")
                  if not utils.cleanHall:
                    print("The guard carefully inspects my work. 'Well I've certainly seen better, but I suppose it's passable. You may proceed.''")
                    utils.cleanHall = True
            elif (verb == "push" or verb == "break") and noun == "prototype" and x == 5 and y == 1:
              validCommand = True
              if not utils.georgeDistracted:
                utils.georgeDistracted = True
                print("I push the construction prototype off its table and it crashes loudly to the floor.")
                print("The large man working across the room jumps out of his seat. He abandons whatever he was working on and immediately starts repairing the broken prototype.")
                print("'Aw, poor thing,' he says, 'I'll fix you up.'")
              else:
                print("The prototype is being lovingly tended to. I couldn't do that now.")

            if ("item" in command or "items" in command) and ("room" in command or "rooms" in command):
                where = library(str(x), str(y))
                __import__(where).listItems()
                validCommand = True
                    
          if len(splitCommand) == 0 or validCommand == False:
            print("Please input a valid command")
            command = input("")
            
while True:
    if os.path.exists('save.py') == True:
        import utils, save
        if save.x == 0 and save.y == 0 and len(save.roomcodes) != 0:
            utils.x = int(save.roomcodes[-1][0])
            utils.y = int(save.roomcodes[-1][-1])
        else:
            utils.x = save.x
            utils.y = save.y
            
        utils.roomlist = save.roomcodes
        utils.cheat = save.cheat
        utils.PlayerKeys = save.PlayerKeys
        utils.advanced = save.advanced
        utils.inventory = save.inventory
        utils.disguise = save.disguise
        utils.GPS = save.GPS
        utils.alarmOn = save.alarmOn
        utils.ventOpen = save.ventOpen
        utils.EMgate = save.EMgate
        utils.cleanHall = save.cleanHall
        utils.georgeDistracted = save.georgeDistracted
        utils.hasOribot = save.hasOribot
        utils.oriBotGPS = save.oriBotGPS
        utils.blockedDoor = save.blockedDoor
        where = library(str(utils.x), str(utils.y))
        if utils.advanced == True:
            __import__(where).fancyDes()
        else:
            __import__(where).basicDes()
        
        if utils.x == 0 and utils.y == 0 and len(save.roomlist) == 0:
            T.intro()  
        os.remove('save.py')
    processLanguage()