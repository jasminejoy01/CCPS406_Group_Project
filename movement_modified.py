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
class direction: ## output: position coordinates
    def __init__(self):
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
        x = x-1
        position = [x,y]
        print(position)
        return position
    
    def left(self):
        global position
        global x
        x = x+1
        position = [x,y]
        print(position)
        return position
    
    def up(self):
        global position
        global y
        y = y-1
        position = [x,y]
        print(position)
        return position
    
    def down(self):
        global position
        global y
        y = y+1
        position = [x,y]
        print(position)
      
class GoTo: #checks
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tr = 0
        self.tl = 0
        self.br = 0
        self.bl = 0
        self.roomWidth = 1
        self.roomLength = 1
        self.floor = []
    
    def move(self, x, y):
        print(self.tr)
        #return cleaningBotStorage
        
    def listItems():
      #open document with room description
      # list documents with code
      pass


def main():
    """Echo the input arguments to standard output"""
    print(direction())
    #GoTo()
    #pass

main()    
