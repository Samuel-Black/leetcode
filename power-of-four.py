from unittest import TestCase

class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    if n == 0:
      return False
    
    while n%4==0:
      n/=4

    return n == 1


solution = Solution()
testCase = TestCase()

test1 = solution.isPowerOfFour(16)
testCase.assertTrue(test1)

test2 = solution.isPowerOfFour(5)
testCase.assertFalse(test2)

test3 = solution.isPowerOfFour(1)
testCase.assertTrue(test3)