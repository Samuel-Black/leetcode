from collections import deque
import unittest
from typing import List

class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

    dq = deque()
    res = []

    for i in range(k):
      while dq and nums[i] >= nums[dq[-1]]:
        dq.pop()
      dq.append(i)

    res.append(nums[dq[0]])

    for i in range(k, len(nums)):
      if dq and dq[0] == i - k:
        dq.popleft()
      while dq and nums[i] >= nums[dq[-1]]:
        dq.pop()

      dq.append(i)
      res.append(nums[dq[0]])

    return res
    # n = len(nums)
    # # res = nums[]
    # # res.sort()
    
    # # dp = []
    # res = []
    # maxStack = [-(10**4+1)] * n
    # maxStack[0] = nums[0]
    
    # if k == 1:
    #   return nums
    
    # # for i in range(1, k-1):
    # #   maxStack[i] = max(maxStack[i-1], nums[i])
    # #   # if nums[i] > maxStack[0]:
    # #   #   maxStack[0] = nums[i]
    # # for i in range(k-1, n):
    # #   # for 
    # #   maxStack[i] = max(maxStack[i-1], nums[i])
    # #   res.append(maxStack[i])
    
    # # left, right = 0, k-1
    # # currentMax = -(10**4+1)
    
    # # for i in range(0, k):
    # #   currentMax = max(nums[i], currentMax)
      
    # # for i in range(0, n):
      
      
    # for i in range(0, (n-k)+1):
    #   currentMax = -(10**4+1)
    #   for j in range(i, i+k):
    #     currentMax = max(nums[j], currentMax)
    #   res.append(currentMax)
    
    # return res
    
solution = Solution()
test = unittest.TestCase()
test1 = solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
test.assertEqual(test1, [3,3,5,5,6,7], test1)
test2 = solution.maxSlidingWindow([1], 1)
test.assertEqual(test2, [1], test2)
test3 = solution.maxSlidingWindow([1,-1], 1)
test.assertEqual(test3, [1,-1], test3)
test4 = solution.maxSlidingWindow([7,2,4], 2)
test.assertEqual(test4, [7,4], test4)
