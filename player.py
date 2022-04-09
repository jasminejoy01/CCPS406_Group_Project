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
    self.keys = []
    #key list: 1 = creator's, 2 = origami, 3 = construction