from typing import List
from unittest import TestCase

class Solution:
  def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    
    dp = []

    

    return dp[-1]

solution = Solution()
testCase = TestCase()

test1 = solution.smallestDivisor([1,2,5,9], 6)
testCase.assertEqual(test1, 5)

test2 = solution.smallestDivisor([44,22,33,11,1], 5)
testCase.assertEqual(test2, 44)