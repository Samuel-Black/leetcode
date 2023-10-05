from collections import defaultdict
from typing import List
from unittest import TestCase

class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    
    majorityA = None
    majorityB = None

    majorityACount = 0
    majorityBCount = 0

    for num in nums:
      if majorityA == num:
        majorityACount+=1
      elif majorityB == num:
        majorityBCount+=1
      elif majorityACount == 0:
        majorityA = num
        majorityACount+=1
        continue
      elif majorityBCount == 0:
        majorityB = num
        majorityBCount+=1
        continue
      else:
        majorityACount-=1
        majorityBCount-=1

    res = []

    for m in [majorityA, majorityB]:
      if nums.count(m) > len(nums)//3:
        res.append(m)

    return res


      


    
  
solution = Solution()
testCase = TestCase()

test1 = solution.majorityElement([3,2,3])
testCase.assertEqual(test1, [3])

test2 = solution.majorityElement([1])
testCase.assertEqual(test2, [1])

test3 = solution.majorityElement([1,2])
testCase.assertEqual(test3, [1,2])

test4 = solution.majorityElement([2,1,1,3,1,4,5,6])
testCase.assertEqual(test4, [1])

