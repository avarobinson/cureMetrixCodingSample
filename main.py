import unittest
import codingSample

class MathTest(unittest.TestCase):

    def testDivisible(self):
        result1 = codingSample.divisible(0,10)
        result2 = codingSample.divisible(5,40)
        result3 = codingSample.divisible(0,3)
        result4 = codingSample.divisible(-40, 40)
        self.assertEqual(result1, [5])
        self.assertEqual(result2, [10,15,20,25,30])
        self.assertEqual(result3, [])
        self.assertEqual(result4, [-30, -25, -20, -15, -10, -5, 5, 10, 15, 20, 25, 30])

    def testFunction(self):
        result1 = codingSample.function(5,2)
        result2= codingSample.function(0, 10)
        result3 = codingSample.function(-1, 10)
        result4 = codingSample.function(400, -20)
        self.assertEqual(result1, 10)
        self.assertEqual(result2, 0)
        self.assertEqual(result3, 0)
        self.assertEqual(result4, 0)

class Game(unittest.TestCase):

    def testGame(self):
        movements = [["up", 1], ["left", 3], ["down", 2]]
        result1 = codingSample.chessboard(movements)
        self.assertEqual(result1, "Total distance traveled: 6\nSpaces away from start: 4")
