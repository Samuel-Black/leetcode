from unittest import TestCase

class Solution:
  def numOfArrays(self, n: int, m: int, k: int) -> int:
        
    
        
solution = Solution()
testCase = TestCase()

test1 = solution.numOfArrays(2, 3, 1)
testCase.assertEqual(test1, 6)

test2 = solution.numOfArrays(5, 2, 3)
testCase.assertEqual(test2, 0)

test3 = solution.numOfArrays(9, 1, 1)
testCase.assertEqual(test3, 1)