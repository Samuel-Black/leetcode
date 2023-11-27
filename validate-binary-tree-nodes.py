from typing import List
from unittest import TestCase

class Solution:
  def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    
    

    return True

solution = Solution()
testCase = TestCase()

test1 = solution.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1])
testCase.assertTrue(test1)

test2 = solution.validateBinaryTreeNodes(4, [1,-1,3,-1], [2,3,-1,-1])
testCase.assertFalse(test2)

test3 = solution.validateBinaryTreeNodes(2, [1,0], [-1,-1])
testCase.assertFalse(test3)