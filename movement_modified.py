# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:11:53 2022

@author: jasmi
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 14:02:08 2022

@author: jasmi
"""

x=0
y=0
position = [x,y]

class direction:
    def __init__(self):
        #self.x = 0
        #self.y = 0
        self.currentRoom = None
        while (True):
            value = input("Please Move:\n")
            if (value == 'n' or value == 'N'):
                self.up()
                # checkIfRoomExists
            elif (value == 's' or value == 'S'):
                self.down()
                # checkIfRoomExists
            elif (value == 'e' or value == 'E'):
                self.right()
                # checkIfRoomExists
            elif (value == 'w' or value == 'W'):
                self.left()
                # checkIfRoomExists
            else:
                print("Please type in either 'n', 's', 'e', or 'w':")
    
    def right(self):
        global position
        global x
        x = x+1
        position = [x,y]
        print(position)
    
    def left(self):
        global position
        global x
        x = x-1
        position = [x,y]
        print(position)
    
    def up(self):
        global position
        global y
        y = y+1
        position = [x,y]
        print(position)
    
    def down(self):
        global position
        global y
        y = y-1
        position = [x,y]
        print(position)
               
direction()