from unittest import TestCase

class Solution:
  def houseOfCards(self, n: int) -> int:
    
    
    
solution = Solution()
testCase = TestCase()

test1 = solution.houseOfCards(16)
testCase.assertEqual(test1, 2)

test2 = solution.houseOfCards(2)
testCase.assertEqual(test2, 1)

test3 = solution.houseOfCards(4)
testCase.assertEqual(test3, 0)