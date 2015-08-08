# SPOJ Classical Problems 
# Url:    http://www.spoj.com/problems/ONP/
# Author: matheusrma

# -*- coding: UTF-8 -*-

import sys

# Adds problem-solving folder to module searching path 
# to enable code modularization
sys.path.append('../../')

import unittest
from util.python.printer import Printer
from util.python.reader import Reader

class Tests(unittest.TestCase):

  def setUp(self):
    self.testSubject = ProblemSolver()

  def testExample1(self):
    self.assertEqual(self.testSubject.run(['(a+(b*c))']), ['abc*+'])  

class ProblemSolver():

  def run(self, input):
    
    return input

# MAIN

def runTests():
  suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
  unittest.TextTestRunner(verbosity = 2).run(suite)

if len(sys.argv) > 1 and sys.argv[1] == 'test':
  runTests();
else:
  reader  = Reader(hasTestCount = True);
  solver  = ProblemSolver();
  printer = Printer(hasLineBetweenPrints = False);

  inputArray = reader.readIntegersFromConsole()

  while inputArray != []:
    solution = solver.run(inputArray)
    printer.printToConsole(solution)
    inputArray = reader.readFromConsole()
