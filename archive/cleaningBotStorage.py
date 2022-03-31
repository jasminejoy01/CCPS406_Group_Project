# -*- coding: utf-8 -*-
# Name: Cleaning bot storage

import objects
#import outdoors_north
import movement_modified

visited = 0 #trigger to tell if room is visited 

description = ''' Cleaning Bot Storage
Door: West (action: unlock)
Items: door, broom
'''

itemshere = [ objects.broom()]

objects.door.isLocked = True
#objects.isAccessible = None 
objects.broom.isPickup = True
objects.broom.examine = True

doorLocked = objects.door.isLocked
broomPickup_ = objects.broom.isPickup

# def nextroom():
#     print('Moving to outdoors_north')
#     import outdoors_north
    
def prevroom():
    print('Moving back to movement_modified')
    import movement_modified

def doorUnlock(doorLocked):
    if doorLocked == True:
        objects.door.isLocked = False
        doorLocked = False
    return doorLocked
 
def broomPickup(broomPickup_):
    if broomPickup_ == True:
        objects.broom.isPickup = True
        print("Picked up broom")
    
def examine():
    action = "description or insight here, possible action sequence ot set up"
    #return action
    
    
