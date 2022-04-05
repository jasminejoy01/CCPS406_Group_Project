import utils
import CreatorOffice

class oriBot:
    def __init__(self):
      self.name = "origamibot"
      self.awake = False
      self.inInventory = False

    def take(self, filename):
        if not self.inInventory:
          if not self.awake:
            print("Oh! It woke up at my touch!")
          self.inInventory = True
          self.awake = True
          utils.inventory[self.name] = filename
          print("I set it on my shoulder. It's hard to tell, but it seems my new little friend is happy to come along for the ride")
        else:
            print("The origami bot is already on my shoulder.")

  #For puzzle 7
    def use(self):
      if utils.x == 5 and utils.y == 3:
        if CreatorOffice.ventOpen == True:
          print("I put the origami bot in the open vent")
        else: 
          print("The little origami bot looks like it wants to squeeze through the vent, but it can't quite fit")
      else:
        print("I'm not quite sure what do with the origami bot here")

    def examine(self):
      if not self.awake:
        print("A small white square with creases running through it. It's hard to believe it can actually move on its own. I nudge it and... oh! It appears to have woken up!")
        self.awake = True
      else: print("A small white square with creases running through it. It folds and unfurls itself to skitter around.")
