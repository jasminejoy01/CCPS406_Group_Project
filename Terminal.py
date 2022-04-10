#Terminals which the player can interact with to unlock rooms, given the right key

import utils

class Terminal:
  def __init__(self, key):
    self.name = "terminal"
    self.key = key;
    self.locked = True;

  def use(self):
    if len(utils.PlayerKeys) == 0:
      print("It seems to require an NFC key that I don't have yet.")
    else:
      if self.key in utils.PlayerKeys:
          print("I scanned my key and the door clicked open.")
          self.locked = False
      else:
        print("It look's like I'll need a key from this deparment's head to unlock it.")


  def examine(self):
    if self.locked:
      print("The terminal reads \n\'LOCKED\'")
    else:
      print("The terminal reads \n'Unlocked'")

class Computer2:
  #Computer in programming lab
  def __init__(self):
    self.name = "computer"

  def use(self):
    if not utils.programminglabOccupied:
        #computer.getSchedule()
        utils.origamiHeadChecker = False
    else:
        print("There are no computers available in this lab. You'll need to get someone to leave...")