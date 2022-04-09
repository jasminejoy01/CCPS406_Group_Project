import utils 
import Item2 as I2

class StorageCloset:
    def disguise():
        print("Description about disguising.")
        utils.disgsuise = True

class Check_Inventory:
    def check():
        print(utils.inventory)

class ServerRoom:
    def smokealarm():
        item = 'wire'
        if utils.programminglabOccupied:
            if item in utils.inventory.keys():
                print("Using copper wire to set off the smoke alarm in Progrmaming Lab.")
                utils.securityPuzzleCheck = True
                print("The fire alarm blares to life. I hear groaning as people shuffle into the hallway.")
            else:
                print("Grab a copper wire from Prototype Workshop!")
                utils.securityPuzzleCheck = False
            
        
        