from typing import List
from unittest import TestCase

class Solution:
  def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    
    intervals.sort(key = lambda x: (x[0],-x[1]))
    # intervals.sort(key=lambda x: x[1], reverse=True)
    # intervals.sort(key=lambda x: x[0])

    n = len(intervals)
    for i in range(n-1, -1, -1):
      for j in range(i-1, -1, -1):
        if intervals[i][1] <= intervals[j][1]:
          intervals.pop(i)
          break

    return len(intervals)

solution = Solution()
testCase = TestCase()

# test1 = solution.removeCoveredIntervals([[1,4],[3,6],[2,8]])
# testCase.assertEqual(test1, 2)

# test2 = solution.removeCoveredIntervals([[1,4],[2,3]])
# testCase.assertEqual(test2, 1)

test3 = solution.removeCoveredIntervals([[1,2],[1,4],[3,4]])
testCase.assertEqual(test3, 1)