from typing import List
from unittest import TestCase

class Solution:
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    
    m = len(maze)
    n = len(maze[0])
    
    directions = [
      (1,0), # up
      (-1,0), # down
      (0,-1), # left
      (0,1), # right
    ]
    
    queue = [(start, 0)]
    seen = set(start)
    
    while queue:
      (curr, distance) = queue.pop()
      if curr in seen:
        continue
      for d in directions:
        
        
      
    
      
solution = Solution()
testCase = TestCase()

test1 = solution.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4])
testCase.assertEqual(test1, 12)

test2 = solution.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [3,2])
testCase.assertEqual(test2, -1)

test3 = solution.shortestDistance([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1])
testCase.assertEqual(test3, -1)