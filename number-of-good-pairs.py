from collections import defaultdict
from typing import List
from unittest import TestCase

class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
        
    numsCount = defaultdict(int)
    pairCount = 0

    for num in nums:
      numsCount[num]+=1
      # if 
      # if dict[num] > 1:
      pairCount += (1*(numsCount[num]-1))
    
    return pairCount

solution = Solution()
testCase = TestCase()

test1 = solution.numIdenticalPairs([1,2,3,1,1,3])
testCase.assertEqual(test1, 4)

test2 = solution.numIdenticalPairs([1,1,1,1])
testCase.assertEqual(test2, 6)

test3 = solution.numIdenticalPairs([1,2,3])
testCase.assertEqual(test3, 0)