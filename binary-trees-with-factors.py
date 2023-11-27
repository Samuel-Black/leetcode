from functools import cache
from typing import List
from unittest import TestCase

class Solution:
  def numFactoredBinaryTrees(self, arr: List[int]) -> int:
    
    @cache
    def dp():

    return dp()

solution = Solution()
testCase = TestCase()

test1 = solution.numFactoredBinaryTrees([2,4])
testCase.assertEqual(test1, 3)

test2 = solution.numFactoredBinaryTrees([2,4,5,10])
testCase.assertEqual(test2, 7)