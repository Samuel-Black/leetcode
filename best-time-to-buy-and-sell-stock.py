from typing import List
from unittest import TestCase

class Solution:
  def maxProfit(self, prices: List[int]) -> int:

    left, right = 0, 1
    maxDiff = 0
    while right < len(prices):
      diff = prices[right]-prices[left]
      if diff > maxDiff:
        maxDiff = diff
      if prices[right] < prices[left]:
        left = right
      right+=1
    return maxDiff
    
solution = Solution()
testCase = TestCase()

test1 = solution.maxProfit([7,1,5,3,6,4])
testCase.assertEqual(test1, 5)

test2 = solution.maxProfit([7,6,4,3,1])
testCase.assertEqual(test2, 0)