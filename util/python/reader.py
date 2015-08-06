# Problem solving python tooling
# Url:    http://www.spoj.com/problems/PRIME1/
# Author: matheusrma

# -*- coding: UTF-8 -*-

class Reader():

  def __init__(self, hasTestCount):
    if hasTestCount:
      self.testCount = input()

  def readFromConsole(self):
    try:
      line = raw_input()
      inputArray = line.split(' ')
      
      for j in range(len(inputArray)):
        inputArray[j] = int(inputArray[j])

      return inputArray    
    except EOFError as error:
      return [];