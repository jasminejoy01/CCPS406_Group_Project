"""
schedule
"""

import time
headstat = []
import utils

#call function when interacting with room computer
# in programming lab or just call it when entering room
class scheduler:
  def __init__(self):
    self.name = "computer"
    self.canTake = False
    self.inInventory = False
    self.description = "This computer appears to be signed in under the name 'Mae Na'"
    self.interactable = True
    self.useText = ""
    self.islocked = False
  
  def examine(self):
    print("This computer appears to be signed in under the name 'Mae Na'")
    print("The desktop background is a picture of a cherry tree in bloom.")
  
  def use(self):
    print("There's a minimized tab. I open it.")
    self.setSchedule()
    
  def setSchedule(self):
      x=0
      while x == 0:
          value = input("Welcome!\nWhose schedule would you like to access?\n1. Dr. Cordelia Weaver\n2. Dr. George Ediface\n3. Dr. Omi Yami\0. Exit\n")
          if value == '1':
              print("Admin Access Required")
              time.sleep(1)
          elif value == '2':
              print("Admin Access Required")
              time.sleep(1)
          elif value == '3':
              print("...")
              time.sleep(1)
              print("Access to schedule #3 granted")
              time.sleep(1)
              print("Upcoming event: Lead meditation in the garden, tomorrow at noon.")
              y=0
              while y == 0:
                  v = input("Switch event time to now? [y/n]")
                  if v.lower() == 'y':
                      time.sleep(1)
                      print("You hear a feminine voice grumbling and rushing out of their office, '...can't respect a simple schedule...'\nI think it's safe to go in there now")
                      utils.PlayerKeys.append(4)
                      y = 1
                      x = 1
                  elif (v == 'N') or (v == 'n'):
                      print("I leave the computer.")
                      y = 1
                  else:
                      print("Please choose: [y/n]")
          elif value == '0':
              x = 1
              print("You've exited the scheduler")
          else:
              print("Error; invalid input")
  
