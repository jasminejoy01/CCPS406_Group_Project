#from Item import Item, Computer
import Item as I
#import room as R
import player as P
import text as T
import utils
import initialize

rooms = ['Private Workshop']
objects = []
currentroomdict = ['00']

player = P.Player()

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
  

def processLanguage(obj=None):        
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
            if (verb == "look"):
                where = library(str(x), str(y))
                __import__(where).basicDes()
                validCommand = True
            if (verb == "cheat"):
                rooms.unlockRooms()
                validCommand = True
            if verb == "help":
                T.help()
                validCommand = True
  
        #2-word commands
        if len(splitCommand) >= 2:
            x = utils.x
            y = utils.y
            if command == "where am i":
                locate = whereami(str(x), str(y))
                print("You are currently in", locate, ".")
                validCommand = True
            if command == "look again":
                where = library(str(x), str(y))
                __import__(where).fancyDes()
                validCommand = True
            noun = splitCommand[1].lower()
            if verb == "read":
                if 'userguide'== noun or 'guide' == noun:
                    T.readUserGuide()
                    validCommand = True
                if 'paper' == noun or 'note' == noun:
                    ################################
                    validCommand = True
            if (verb == "exam") | (verb == "examine"):
                #Check that noun is a valid object
                obj.examine()
                validCommand = True
            if (verb == "take"):
                #Check that noun is a valid object
                obj.take()
                validCommand = True
            if (verb == "use"):
                obj.use()
                validCommand = True
                    
        #3-word commands
        if len(splitCommand) == 3:
            if (verb == "read" or verb == "exam" or verb == "examine"):
                if splitCommand[1].lower() == "user's" and splitCommand[2].lower() == "guide":
                    T.readUserGuide()
                    validCommand = True
                if splitCommand[1].lower() == "sticky" and splitCommand[2].lower() == "notes":
                    print("The notes mostly contain sketches of strange robots and bizarre contraptions, surrounded by hearts")
                    validCommand = True
    
        #else
        if len(splitCommand) == 0 or not validCommand:
            print("Please input a valid command")
            command = input(" ")
            
# print("What should I do?")

while True:
    processLanguage()
    