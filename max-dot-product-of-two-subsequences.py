from functools import cache
from typing import List
from unittest import TestCase

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(use, dp(i + 1, j), dp(i, j + 1))
            
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        return dp(0, 0)
    # m = len(nums1)
    # n = len(nums2)
    
    # dp = [[0] * (m+1) for _ in range(0, n)]
    
    # # for i in range(0, m):
    # #   for j in range(0, n):
        
    
    # return 0
    
    # @cache
    # def dp(n1: List[int], n2: List[int]):
    #   currMax = -float("inf")
    #   for i in range(0, len(n1)):
    #     for j in range(0, len(n2)):
    #       currMax = max(currMax, dp())
          
    #   return max(dp())
      
    # return dp(nums1, nums2)
      
        
solution = Solution()
testCase = TestCase()

test1 = solution.maxDotProduct([2,1,-2,5], [3,0,-6])
testCase.assertEqual(test1, 18)

test2 = solution.maxDotProduct([3,-2], [2,-6,7])
testCase.assertEqual(test2, 21)

test3 = solution.maxDotProduct([-1,-1], [1,1])
testCase.assertEqual(test3, -1)