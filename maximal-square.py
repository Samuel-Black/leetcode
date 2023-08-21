from typing import List
import unittest

class Solution:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    
    n = len(matrix)
    m = len(matrix[0])
    
    dp = [[0] * (m) for _ in range(n)]
    
    
    
    return dp
    
    
solution = Solution()
test = unittest.TestCase()

test1 = solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
test.assertEqual(test1, 4)

test2 = solution.maximalSquare([["0","1"],["1","0"]])
test.assertEqual(test2, 1)

test3 = solution.maximalSquare([["0"]])
test.assertEqual(test3, 0)
