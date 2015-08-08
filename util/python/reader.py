# Problem solving python tooling
# Url:    http://www.spoj.com/problems/PRIME1/
# Author: matheusrma

# -*- coding: UTF-8 -*-

class Reader():
  """Responsible for reading input from console    
  """

  def __init__(self, hasTestCount):
    if hasTestCount:
      self.testCount = input()

  def readIntegersFromConsole(self):
    """ Will read a single line of integers and return them as an array
    """
    try:
      line       = raw_input()
      inputArray = line.split(' ')
      
      for j in range(len(inputArray)):
        inputArray[j] = int(inputArray[j])

      return inputArray    
    except EOFError as error:
      return [];

  def readFromConsole(self):
    """ Will read a single line and return strings in an array
    """

    try:
      line       = raw_input()
      inputArray = line.split(' ')

      return inputArray    
    except EOFError as error:
      return [];