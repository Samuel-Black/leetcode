from typing import List
from unittest import TestCase


class Solution:
  def minTaps(self, n: int, ranges: List[int]) -> int:
    
    # left = right = 0
    
    # ranges.sort(reverse=True)
    
    # currentSum = 0
    
    # for i in range(0, n+1):
    #   currentSum += ranges[i] + 1 if ranges[i] > 0 else 0
    #   if currentSum >= n:
    #     return i + 1
    
    # stack = []
    # seen = set()
    
    # for i in range(0, n+1):
    #   if i - ranges[i] <= 0:
    #     stack.append((i, 1))
    #     seen.add(i)
    
    # while stack:
    #   (i, numTaps) = stack.pop()
    #   if ranges[i] + i >= n:
    #     return numTaps
    #   for j in range(i, min(i + ranges[i] + 2, n+1)):
    #     if j not in seen and ranges[j] > 0:
    #       stack.append((j, numTaps+1))
    #       seen.add(j)
    # return -1
    numTaps = 0
    left = right = 0
    
    while right < n + 1:
      leftRange = ranges[left]
      right+=1
    
    return numTaps
    
solution = Solution()
test = TestCase()

test1 = solution.minTaps(5, [3,4,1,1,0,0])
test.assertEqual(test1, 1)

test2 = solution.minTaps(3, [0,0,0,0])
test.assertEqual(test2, -1)

test3 = solution.minTaps(7, [1,2,1,0,2,1,0,1])
test.assertEqual(test3, 3)

test4 = solution.minTaps(8, [4,0,0,0,0,0,0,0,4])
test.assertEqual(test4, 2)

test5 = solution.minTaps(8, [4,0,0,0,4,0,0,0,4])
test.assertEqual(test5, 1)