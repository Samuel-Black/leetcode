from functools import cache
from unittest import TestCase


class Solution:
  def numWays(self, steps: int, arrLen: int) -> int:
    @cache
    def dp(curr, remain):
      if remain == 0:
        if curr == 0:
          return 1
        
        return 0
      
      ans = dp(curr, remain - 1)
      if curr > 0:
        ans = (ans + dp(curr - 1, remain - 1)) % MOD
      
      if curr < arrLen - 1:
        ans = (ans + dp(curr + 1, remain - 1)) % MOD
          
      return ans
    
    MOD = 10 ** 9 + 7
    return dp(0, steps)
    
    
solution = Solution()
testCase = TestCase()

test1 = solution.numWays(3, 2)
testCase.assertEqual(test1, 4)

test2 = solution.numWays(2, 4)
testCase.assertEqual(test2, 2)

test3 = solution.numWays(4, 2)
testCase.assertEqual(test3, 2)
