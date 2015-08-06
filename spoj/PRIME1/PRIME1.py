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
    self.assertEqual(self.testSubject.run([1,10]), [2,3,5,7])  

  def testExample2(self):
    self.assertEqual(self.testSubject.run([3,5]), [3,5])  
  
  def testSamePrime(self):
    self.assertEqual(self.testSubject.run([17,17]), [17])  

class ProblemSolver():

  def isPrime(self, num):
    if num == 1:
      return False

    for i in range(2, num):
      # There are no divisors after the square root of a given number
      if i > sqrt(num):
        break

      if num % i == 0:
        return False

    return True

  def run(self, input):
    
    solution = []

    start = input[0]
    end   = input[1]

    for i in range(start, end + 1):
      if self.isPrime(i):
        solution.append(i);

    return solution

# MAIN

def runTests():
  suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
  unittest.TextTestRunner(verbosity = 2).run(suite)

if len(sys.argv) > 1 and sys.argv[1] == 'test':
  runTests();
else:
  reader  = Reader(True);
  solver  = ProblemSolver();
  printer = Printer();

  inputArray = reader.readFromConsole()

  while inputArray != []:
    solution = solver.run(inputArray)
    printer.printToConsole(solution)
    inputArray = reader.readFromConsole()
