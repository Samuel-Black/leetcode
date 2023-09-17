from functools import cache
from typing import List
from unittest import TestCase

class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    
    @cache
    def getDistance(x1, y1, x2, y2):
      return abs(x1-x2) + abs(y1-y2)
    
    m = len(points)
    n = len(points[0])
    
    dp = [[0] * (m) for _ in range(m)]
    
    for i in range()
    
    for i in range(0, m):
      print()
    
    return dp
    
solution = Solution()
testCase = TestCase()

test1 = solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
testCase.assertEqual(test1, 20)

test2 = solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]])
testCase.assertEqual(test2, 18)