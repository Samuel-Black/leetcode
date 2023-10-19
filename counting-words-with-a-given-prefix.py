from typing import List
from unittest import TestCase

class Solution:
  def prefixCount(self, words: List[str], pref: str) -> int:
    
    res = 0
    n  = len(pref)
    for word in words:
      if word[0:n] == pref:
        res+=1

    return res

solution = Solution()
testCase = TestCase()

test1 = solution.prefixCount(["pay","attention","practice","attend"], "at")
testCase.assertEqual(test1, 2)

test2 = solution.prefixCount(["leetcode","win","loops","success"], "code")
testCase.assertEqual(test2, 0)