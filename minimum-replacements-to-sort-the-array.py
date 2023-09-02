from unittest import TestCase
from typing import List

class Solution:
  def minimumReplacement(self, nums: List[int]) -> int:
    
    
    
solution = Solution()
test = TestCase

test1 = solution.minimumReplacement([3,9,3])
test.assertEqual(test1, 2)

test2 = solution.minimumReplacement([1,2,3,4,5])
test.assertEqual(test2, 0)