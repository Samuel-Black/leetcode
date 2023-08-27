from typing import List
from unittest import TestCase

class Solution:
  def canCross(self, stones: List[int]) -> bool:
    
    n = len(stones)
    
    # index in stones list, cost of jump to get to that stone
    stack = [(0, 0)]
    seen = set()
    seen.add((0,0))
    
    while stack:
      i, k = stack.pop()
      if i == n-1:
        return True
      for j in range(i+1, n):
        cost = stones[j] - stones[i]
        if -1 <= k - cost <= 1:
          if (j, cost) not in seen:
            stack.append((j, cost))
            seen.add((j, cost))
        elif k - cost < -1:
          break
       
    return False
    
    
solution = Solution()
test = TestCase()

test1 = solution.canCross([0,1,3,5,6,8,12,17])
test.assertEqual(test1, True)

test2 = solution.canCross([0,1,2,3,4,8,9,11])
test.assertEqual(test2, False)