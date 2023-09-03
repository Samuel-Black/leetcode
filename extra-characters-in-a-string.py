from functools import cache
from typing import List
from unittest import TestCase

class Solution:
  def minExtraChar(self, s: str, dictionary: List[str]) -> int:
    n, dictionary_set = len(s), set(dictionary)
    @cache
    def dp(start):
      if start == n:
        return 0
      # To count this character as a left over character 
      # move to index 'start + 1'
      ans = dp(start + 1) + 1
      for end in range(start, n):
        curr = s[start: end + 1]
        if curr in dictionary_set:
          ans = min(ans, dp(end + 1))
      return ans
        
    return dp(0)
      
    
solution = Solution()
test = TestCase()

test1 = solution.minExtraChar("leetscode", ["leet","code","leetcode"])
test.assertEqual(test1, 1)

test2 = solution.minExtraChar("sayhelloworld", ["hello","world"])
test.assertEqual(test2, 3)