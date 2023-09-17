from typing import List
from unittest import TestCase

class Solution:
  def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
      
    n = len(nums)
    nums.sort()
    
    res = []
    
    for query in queries:
      count = 0
      currentSum = 0
      while count < n:
        currentSum += nums[count]
        if currentSum > query:
          break
        count+=1
      res.append(count)
    return res
      
solution = Solution()
testCase = TestCase()

test1 = solution.answerQueries([4,5,2,1], [3,10,21])
testCase.assertEqual(test1, [2,3,4])

test2 = solution.answerQueries([2,3,4,5], [1])
testCase.assertEqual(test2, [0])