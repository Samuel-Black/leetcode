from typing import List
import unittest


class Solution:
  def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
    
    
    
solution = Solution()

test = unittest.TestCase()

test1 = solution.maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]])
test.assertEqual(test1, 4)

test2 = solution.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])
test.assertEqual(test2, 5)

test3 = solution.maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])
test.assertEqual(test3, 5)