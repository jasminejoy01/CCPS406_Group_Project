import numpy
import text as T

roomdict = { # [desc, xcoord, ycoord, code]
   0: ["Private Workshop"           , 0, 0, "PrivateWorkshop"],
  10: ["Cleaning Bot Storage"       , 1, 0, "CleaningBotStorage"],
  11: ["Construction Bot Storage"   , 1, 1, "ConstructionBotStorage"],               
  12: ["Origami Bot Storage"        , 1, 2, "OrigamiBotStorage"],
  20: ["Outdoors (north)"           , 2, 0, "OutdoorsNorth"],
  21: ["Outdoors (middle)"          , 2, 1, "OutdoorsMiddle"],                  
  22: ["Outdoors (south)"           , 2, 2, "OutdoorsSouth"],
  23: ["Storage lost & found"       , 2, 3, "Storage"],
  24: ["Hallway (section 6)"        , 2, 4, "Hallway6"],
  25: ["Exit"                       , 2, 5, "Exit"],
  30: ["Greenspace (break area)"    , 3, 0, "Greenspace"],
  31: ["Building Entrance/Exit"     , 3, 1, "BuildingEntranceExit"],
  32: ["Programming Lab"            , 3, 2, "ProgrammingLab"],
  33: ["Construction Head's Office" , 3, 3, "ConstructionHeadOffice"],
  34: ["Hallway (section 5)"        , 3, 4, "Hallway5"],
  35: ["Security"                   , 3, 5, "Security"],
  40: ["Bot testing: simple tasks"  , 4, 0, "BotTesting"],
  41: ["Hallway (section 1)"        , 4, 1, "Hallway1"],
  42: ["Hallway (section 2)"        , 4, 2, "Hallway2"],
  43: ["Hallway (section 3)"        , 4, 3, "Hallway3"],
  44: ["Hallway (section 4)"        , 4, 4, "Hallway4"],
  45: ["Origami Head's Office"      , 4, 5, "OrigamiHeadOffice"],
  50: ["Bot testing:Obstacle course", 5, 0, "BotTestingObstacle"],
  51: ["Prototype Workshop"         , 5, 1, "PrototypeWorkshop"],
  52: ["3D Printing Lab"            , 5, 2, "PrintingLab"],
  53: ["Creator's Office"           , 5, 3, "CreatorOffice"],
  54: ["Server Room"                , 5, 4, "Server"]
}

#visited = numpy.zeros(len(roomdict))
visited = [0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 , 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 , 0, 0, 0, 0, 0 , 0, 0]

if len(visited) != len(roomdict):
    print("initialize.py : Array length does not match")

T.intro()
x = 0
y = 0

GPS = True
advanced = False  #Determines description complexity
PlayerKeys = [] #Creator's key
inventory = {}
cheat = False
disguise = False
programminglabOccupied = True
origamiHeadChecker = False     #puzzle6.py
puzzle4 = False                #puzzle4.py
constructionChecker = False    #puzzle4.py
constructionBotChecker = False    #puzzle4.py
prototypeChecker = False      #puzzle4.py
securityPuzzleCheck = False   # sequence of events, triggers programminglabOccupied = False

print("Write a command")