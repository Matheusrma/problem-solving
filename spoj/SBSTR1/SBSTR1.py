# SPOJ Classical Problems 
# Url:    http://www.spoj.com/problems/PRIME1/
# Author: matheusrma

# -*- coding: UTF-8 -*-

import sys

# Adds problem-solving folder to module searching path 
# to enable code modularization
sys.path.append('../../')

import unittest
from math import sqrt
from util.python.printer import Printer
from util.python.reader import Reader

class Tests(unittest.TestCase):

  def setUp(self):
    self.testSubject = ProblemSolver()

  def testExample1(self):
    self.assertEqual(self.testSubject.run(['1010110010', '10110']), [1])  
  
  def testExample2(self):
    self.assertEqual(self.testSubject.run(['1110111011', '10011']), [0])  
    
class ProblemSolver():

  def run(self, input):
    if input[0].find(input[1]) != -1:
      return [1]
    else:
      return [0]

# MAIN

def runTests():
  suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
  unittest.TextTestRunner(verbosity = 2).run(suite)

if len(sys.argv) > 1 and sys.argv[1] == 'test':
  runTests();
else:
  reader  = Reader(hasTestCount = False);
  solver  = ProblemSolver();
  printer = Printer(hasLineBetweenPrints = False);

  inputArray = reader.readFromConsole()

  while inputArray != []:
    solution = solver.run(inputArray)
    printer.printToConsole(solution)
    inputArray = reader.readFromConsole()
