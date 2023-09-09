from typing import List
from unittest import TestCase

class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    
    dp = [0] * (target+1)
    
    # base case
    dp[0] = 1
    
    for i in range(1, target+1):
      
      for num in nums:
        if i - num >= 0:
          dp[i] += dp[i-num]
    
    return dp[target]
    # nums.sort()
    # # n = len(nums)
    # combinations = set()
    # # seen = set()
    # # numsSet = set(nums)
    
    # stack = set((x,) for x in nums)
    
    # while stack:
    #   val = stack.pop()
    #   if sum(val) == target:
    #     combinations.add(val)
    #   elif sum(val) < target:
    #     for num in nums:
    #       if sum(val) + num > target:
    #         break
    #       newVal = val + (num,)
    #       stack.add(newVal)
    #       # if newVal not in seen:
            
    # return len(combinations)
    
solution = Solution()
testCase = TestCase()

test1 = solution.combinationSum4([1,2,3], 4)
testCase.assertEqual(test1, 7)

test2 = solution.combinationSum4([9], 3)
testCase.assertEqual(test2, 0)

test3 = solution.combinationSum4([4,2,1], 32)
testCase.assertEqual(test3, 39882198)