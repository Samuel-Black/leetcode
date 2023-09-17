from collections import defaultdict
from unittest import TestCase

class Solution:
  def minDeletions(self, s: str) -> int:
    
    counts = defaultdict(int)
    overlaps = defaultdict(int)
    
    for c in s:
      if c not in counts:
        counts[c] = 0
      counts[c]+=1
      
    for i in counts.values():
      
      
    # for c in s:
    #   if overlaps[counts[c]] > 0:
    #     overlaps[counts[c]] -= 1
    #   counts[c] += 1
    #   overlaps[counts[c]] += 1
      
    #   if overlaps[counts[c]]
      
    return 0
    
solution = Solution()
testCase = TestCase()

test1 = solution.minDeletions("aab")
testCase.assertEqual(test1, 0)

test2 = solution.minDeletions("aaabbbcc")
testCase.assertEqual(test2, 2)

test3 = solution.minDeletions("ceabaacb")
testCase.assertEqual(test3, 2)