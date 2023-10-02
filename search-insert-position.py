

from typing import List
from unittest import TestCase

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:

    def binarySearch(target: int):
      left, right = 0, len(nums)-1

      while left <= right:
        mid = (right + left)//2
        # If x is greater, ignore left half
        if nums[mid] == target:
          return mid
        if target < nums[mid]:
          right = mid - 1
        # If x is smaller, ignore right half
        else:
          left = mid + 1
      return left
    
    return binarySearch(target)


solution = Solution()
testCase = TestCase()

test1 = solution.searchInsert([1,3,5,6], 5)
testCase.assertEqual(test1, 2)

test2 = solution.searchInsert([1,3,5,6], 2)
testCase.assertEqual(test2, 1)

test3 = solution.searchInsert([1,3,5,6], 7)
testCase.assertEqual(test3, 4)