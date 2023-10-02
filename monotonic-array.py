from typing import List
from unittest import TestCase

class Solution:
  def isMonotonic(self, nums: List[int]) -> bool:
    
    n = len(nums)
    # lastNum = 0
    increasing = False
    decreasing = False

    for i in range(1, n):
      remainder = nums[i-1] - nums[i]
      if increasing and remainder > 0:
        return False
      if decreasing and remainder < 0:
        return False
      if not increasing and not decreasing and remainder != 0:
        if remainder > 0:
          decreasing = True
        else:
          increasing = True
      # lastNum = remainder

    return True

solution = Solution()
testCase = TestCase()

test1 = solution.isMonotonic([1,2,2,3])
testCase.assertEqual(test1, True)

test2 = solution.isMonotonic([6,5,4,4])
testCase.assertEqual(test2, True)

test3 = solution.isMonotonic([1,3,2])
testCase.assertEqual(test3, False)

test4 = solution.isMonotonic([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5])
testCase.assertEqual(test4, False)