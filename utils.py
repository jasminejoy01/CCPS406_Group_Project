# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:06:38 2022

@author: jasmi
"""

import sys
import initialize
import os

roomsvisited = initialize.visited

x = initialize.x
y = initialize.x

GPS = initialize.GPS
advanced = initialize.advanced  #Determines description complexity
PlayerKey1 = initialize.PlayerKey1 #Creator's key
inventory = initialize.inventory #Inventory list
cheat = initialize.cheat

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
            arr = initialize.visited
            arr = arr.tolist()
            
            arraylist = ['## rooms visited\n', 
                         'visited =', str(arr)+"\n", 
                         '## current location\n', 
                         'x = ', str(initialize.x)+"\n" , 
                         'y = ', str(initialize.y)+"\n" , 
                         'roomcodes = ', str(roomcodes)+"\n", 
                         '## current inventory\n', 
                         'inventory = ', str(inventory)+"\n",
                         '## keys\n', 
                         'GPS = ', str(GPS)+"\n" ,
                         'advanced = ', str(advanced)+"\n" ,
                         'PlayerKey1 = ', str(PlayerKey1)+"\n" ,
                         'cheat = ', str(cheat)+"\n" 
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