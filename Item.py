import utils
import time

class Item:
    def __init__(self, name, canTake, inInventory, description, interactable, useText):
        self.name = name
        self.canTake = canTake
        self.inInventory = False
        self.description = description
        self.interactable = True
        self.useText = useText

    def take(self, filename):
        if self.canTake:
            self.inInventory = True
            utils.inventory[self.name] = filename
            print("I picked up the {}.".format(self.name))
        else:
            print("I can't do that.")

    def drop(self):
        if self.name in utils.inventory.keys():
            self.inInventory = False
            utils.inventory.pop(self.name)
            print("I remove the {} from my inventory.".format(self.name))
        else:
            print("I can't do that.")
            
    def examine(self):
        print(self.description)

    def use(self):
        if self.interactable:
            print(self.useText)
        else:
            print("I can't do anything with this")

