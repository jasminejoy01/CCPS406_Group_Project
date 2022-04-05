import sys
import initialize
import os

roomsvisited = initialize.visited

x = initialize.x
y = initialize.x

GPS = initialize.GPS
advanced = initialize.advanced  #Determines description complexity
PlayerKeys = initialize.PlayerKeys #Creator's key
inventory = initialize.inventory #Inventory list
cheat = initialize.cheat
disguise = initialize.disguise
programminglabOccupied = initialize.programminglabOccupied

origamiHeadChecker = initialize.origamiHeadChecker
puzzle4 = initialize.puzzle4
constructionChecker = initialize.constructionChecker
constructionBotChecker = initialize.constructionBotChecker
prototypeChecker = initialize.prototypeChecker
securityPuzzleCheck = initialize.securityPuzzleCheck

def exitgame(roomcodes):
    print("Are you sure you want to quit the game?")
    response = input()
    response = response.lower()
    if response == "yes" or response == "y":
        print("Press 's' to save game, 'n' to quit anyway.")
        saveinput = input()
        
        my_file = 'save.py'
        
        if os.path.isfile(my_file) == True:
            os.remove(my_file)
        if saveinput == 's':
            #arr = roomsvisited.tolist()
            
            arraylist = ['## rooms visited\n', 
                         'visited =', str(roomsvisited)+"\n", 
                         '## current location\n', 
                         'x = ', str(initialize.x)+"\n" , 
                         'y = ', str(initialize.y)+"\n" , 
                         'roomcodes = ', str(roomcodes)+"\n", 
                         '## current inventory\n', 
                         'inventory = ', str(inventory)+"\n",
                         '## keys\n', 
                         'GPS = ', str(GPS)+"\n" ,
                         'advanced = ', str(advanced)+"\n" ,
                         'PlayerKey1 = ', str(PlayerKeys)+"\n" ,
                         'cheat = ', str(cheat)+"\n",
                         'disguise = ', str(disguise)+"\n",
                         'origamiHeadChecker = ', str(origamiHeadChecker)+"\n",
                         'puzzle4 = ', str(programminglabOccupied)+"\n",
                         'constructionChecker = ', str(constructionChecker)+"\n",
                         'constructionBotChecker = ', str(constructionBotChecker)+"\n",
                         'prototypeChecker = ', str(prototypeChecker)+"\n",
                         'securityPuzzleCheck = ', str(securityPuzzleCheck)+"\n"
                         ]
            
            f = open(my_file, 'w')
            for each in arraylist:
                f.write(each)
            f.close()
            
            sys.exit()
        if saveinput == 'n':
            sys.exit()
    else:
        pass