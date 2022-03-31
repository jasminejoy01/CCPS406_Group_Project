# -*- coding: utf-8 -*-
"""
Player
"""

class Player(object):
  def __init__(self):
    self.x = 5
    self.y = 5
    self.GPS = False
    self.advanced = False  #Determines description complexity
    self.key1 = False #Creator's key
    
  def moveNorth(self, rooms):
    if rooms[self.x][self.y].northDoor:
      if not rooms[self.x][self.y + 1].locked:
        self.y = self.y + 1
        print(rooms[self.x][self.y].name)
      else: print("I can't go that way yet")
    else: print("There's no door that way")

  def moveEast(self, rooms):
    if rooms[self.x][self.y].eastDoor:
      if not rooms[self.x + 1][self.y].locked:
        self.x = self.x + 1
        print(rooms[self.x][self.y].name)
      else: print("I can't go that way yet")
    else: print("There's no door that way")

  def moveSouth(self, rooms):
    if rooms[self.x][self.y].southDoor:
      if not rooms[self.x][self.y - 1].locked:
        self.y = self.y - 1
        print(rooms[self.x][self.y].name)
      else: print("I can't go that way yet")
    else: print("There's no door that way")

  def moveWest(self, rooms):
    if rooms[self.x][self.y].westDoor:
      if not rooms[self.x - 1 ][self.y].locked:
        self.x = self.x - 1
        print(rooms[self.x][self.y].name)
      else: print("I can't go that way yet")
    else: print("There's no door that way")
