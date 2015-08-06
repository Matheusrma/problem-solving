# SPOJ Classical Problem TEST 
# Url:    http://www.spoj.com/problems/TEST/
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

  def testEmpty(self):
    self.assertEqual(self.testSubject.run([]), [])

  def testOnly42(self):
    self.assertEqual(self.testSubject.run([42]), [])

  def testNumberGroup(self):
    self.assertEqual(self.testSubject.run([1,2,88,42,99]), [1,2,88])  

class ProblemSolver():

  def run(self, input):
    solution = [];

    for item in input:
      if (item == 42):
        break
      solution.append(item)

    return solution

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

  inputArray = reader.readIntegersFromConsole()

  while inputArray != []:
    solution = solver.run(inputArray)
    if (solution == []):
      break
    printer.printToConsole(solution)
    inputArray = reader.readFromConsole()


