# Problem solving python tooling 
# Author: matheusrma

# -*- coding: UTF-8 -*-

class Printer():
  """Responsible for printing to console    
  """

  def __init__(self, hasLineBetweenPrints = True):
    self.hasLineBetweenPrints = hasLineBetweenPrints

  def printToConsole(self, array):
    for item in array:
      print item

    if self.hasLineBetweenPrints:
      print 

