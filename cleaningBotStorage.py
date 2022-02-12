# -*- coding: utf-8 -*-
# Name: Cleaning bot storage

import objects
#import position from movement_modified

description = ''' Cleaning Bot Storage
Door: West (action: unlock)
Items: broom
'''

class cleaningBots(objects.item):
    def __init__(self):
        objects.isAccessible = None 
        objects.isPickup = True
        objects.isLocked = None
        objects.examine = True
        self.items = [ objects.broom()]
    
    def examine():
        # return output
        pass
    
    def unlock():
        #return action
        pass
    
