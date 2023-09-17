from typing import List
from unittest import TestCase

class Solution:
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    
    res = 0
    
    queue = []
    seen = set()
    
    directions = [
      (1, 0), # up
      (-1, 0), # down
      (0, 1), # right
      (0, -1) # left
    ]
    
    while queue:
      
      for directions in directions:
      
    
    return res
    
    
solution = Solution()
testCase = TestCase()

test1 = solution.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])
testCase.assertEqual(test1, 2)

test2 = solution.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]])
testCase.assertEqual(test2, 1)

test3 = solution.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])
testCase.assertEqual(test3, 0)