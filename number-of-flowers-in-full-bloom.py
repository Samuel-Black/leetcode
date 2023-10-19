from bisect import bisect_right
from collections import defaultdict
from typing import List
from unittest import TestCase

class Solution:
  def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
    
    # flowersBloomed = defaultdict(int)

    starts, ends = [], []

    for start, end in flowers:
      starts.append(start)
      ends.append(end+1)

    starts.sort()
    ends.sort()
    res = []

    for person in people:
      i = bisect_right(starts, person)
      j = bisect_right(ends, person)
      res.append(i-j)

    return res



solution = Solution()
testCase = TestCase()

test1 = solution.fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11])
testCase.assertEqual(test1, [1,2,2,2])

test2 = solution.fullBloomFlowers([[1,10],[3,3]], [3,3,2])
testCase.assertEqual(test2, [2,2,1])