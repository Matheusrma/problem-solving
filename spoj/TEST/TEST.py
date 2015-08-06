# SPOJ Classical Problem TEST 
# Url:    http://www.spoj.com/problems/TEST/
# Author: matheusrma

# -*- coding: UTF-8 -*-

import unittest
import sys

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

def runTests():
  suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
  unittest.TextTestRunner(verbosity = 2).run(suite)

if len(sys.argv) > 1 and sys.argv[1] == 'test':
  runTests();
else:
  



