from typing import List
from unittest import TestCase

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]
    # currMajority = nums[0]
    # count = 1
    # currMajorityCount = 0

    # for i in range(1, len(nums)):
    #   if nums[i] != nums[i-1]:
    #     count = 1
    #   else:
    #     count += 1
    #   if count > currMajorityCount:
    #     currMajorityCount = count
    #     currMajority = nums[i]
    # return currMajority
    

solution = Solution()
testCase = TestCase()

test1 = solution.majorityElement([3,2,3])
testCase.assertEqual(test1, 3)

test2 = solution.majorityElement([2,2,1,1,1,2,2])
testCase.assertEqual(test2, 2)