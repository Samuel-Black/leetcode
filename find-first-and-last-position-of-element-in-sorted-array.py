from typing import List
from unittest import TestCase

class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    
    def binarySearch(target: int) -> List[int]:
      n = len(nums)
      left, right = 0, n-1

      while left <= right:
        mid = (left+right)//2
        if target == nums[mid]:
          l = r = mid
          while (l >= 0 and nums[l] == target) or (r < n and nums[r] == target):
            if l >= 0 and nums[l] == target:
              l-=1
            if r < n and nums[r] == target:
              r+=1
          return [max(0,l+1), min(n-1, r-1)]
        elif nums[mid] > target:
          right = (mid-1)
        else:
          left = (mid+1)
      return [-1, -1]

    return binarySearch(target)
  
solution = Solution()
testCase = TestCase()

test1 = solution.searchRange([5,7,7,8,8,10], 8)
testCase.assertEqual(test1, [3,4])

test2 = solution.searchRange([5,7,7,8,8,10], 6)
testCase.assertEqual(test2, [-1,-1])

test3 = solution.searchRange([], 0)
testCase.assertEqual(test3, [-1,-1])

test4 = solution.searchRange([1], 1)
testCase.assertEqual(test4, [0,0])

test5 = solution.searchRange([2,2], 3)
testCase.assertEqual(test5, [-1,-1])

test5 = solution.searchRange([1,2,3], 1)
testCase.assertEqual(test5, [0,0])