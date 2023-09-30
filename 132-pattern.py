from typing import List
from unittest import TestCase

class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
      return False
    mins = [0] * n
    mins[0] = nums[0]
    stack = []
    for i in range(1, n):
      mins[i] = min(mins[i-1], nums[i])

    for j in range(n-1, -1, -1):
      # i needs to be less than j, so if j is less than the mins arr, it can't meet the condition so continue 
      if nums[j] <= mins[j]:
        continue
      # 
      while stack and stack[-1] <= mins[j]:
        stack.pop()
      if stack and stack[-1] < nums[j]:
        return True
      stack.append(nums[j])
    return False


solution = Solution()
testCase = TestCase()

test1 = solution.find132pattern([1,2,3,4])
testCase.assertEqual(test1, False)

test2 = solution.find132pattern([3,1,4,2])
testCase.assertEqual(test2, True)

test3 = solution.find132pattern([-1,3,2,0])
testCase.assertEqual(test3, True)

test4 = solution.find132pattern([3,5,0,3,4])
testCase.assertEqual(test4, True)