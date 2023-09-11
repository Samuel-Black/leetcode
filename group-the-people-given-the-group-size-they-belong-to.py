from typing import List
from unittest import TestCase

class Solution:
  def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
      
    res = []
    n = len(groupSizes)
    currentGroups = {}
    
    for i in range(0, n):
      if groupSizes[i] not in currentGroups:
        currentGroups[groupSizes[i]] = [[]]
      elif len(currentGroups[groupSizes[i]][-1]) >= groupSizes[i]:
        currentGroups[groupSizes[i]].append([])
      currentGroups[groupSizes[i]][-1].append(i)
      
    
    for k, v in sorted(currentGroups.items(), key=lambda item: item[0]):
      res.extend(v)
      
    return res
      
solution = Solution()
testCase = TestCase()

test1 = solution.groupThePeople([3,3,3,3,3,1,3])
testCase.assertEqual(test1, [[5],[0,1,2],[3,4,6]])

test2 = solution.groupThePeople([2,1,3,3,3,2])
testCase.assertEqual(test2, [[1],[0,5],[2,3,4]])