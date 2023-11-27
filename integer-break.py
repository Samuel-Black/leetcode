from functools import cache
from unittest import TestCase

class Solution:
  def integerBreak(self, n: int) -> int:
    
    @cache
    def dp(num: int) -> int:
      
      if num <= 3:
        return num
      
      res = num
      for i in range(2, num):
        res = max(res, i * dp(num - i))
        
      return res    
    
    if n <= 3:
      return n - 1
    return dp(n)

solution = Solution()
testCase = TestCase()

test1 = solution.integerBreak(2)
testCase.assertEqual(test1, 1)

test2 = solution.integerBreak(10)
testCase.assertEqual(test2, 36)