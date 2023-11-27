from typing import List
from unittest import TestCase

class Solution:
  def checkStraightLine(self, coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):
      x, y = coordinates[i]
      if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
        return False

    return True
    
    # while start < end:
    #   difference 

solution = Solution()
testCase = TestCase()

test1 = solution.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
testCase.assertTrue(test1)

test2 = solution.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
testCase.assertFalse(test2)

test3 = solution.checkStraightLine([[1,2],[2,3],[3,5]])
testCase.assertFalse(test3)

test4 = solution.checkStraightLine([[0,0],[0,1],[0,-1]])
testCase.assertTrue(test4)

test5 = solution.checkStraightLine([[1,-8],[2,-3],[1,2]])
testCase.assertFalse(test5)

