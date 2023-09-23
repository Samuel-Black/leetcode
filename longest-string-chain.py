from collections import defaultdict
from functools import cache
from typing import List
from unittest import TestCase

class Solution:
  def longestStrChain(self, words: List[str]) -> int:

    words.sort(key=len)
    dp = defaultdict(int)
    maxPredecessors = 1
    for word in words:
      dp[word] = 1
      for i in range(0, len(word)):
        temp = word[:i] + word[i+1:]
        if temp in dp:
          dp[word] = max(dp[word], dp[temp] + 1)
          maxPredecessors = max(maxPredecessors, dp[word])
    
    return maxPredecessors
    
solution = Solution()
testCase = TestCase()

test1 = solution.longestStrChain(["a","b","ba","bca","bda","bdca"])
# testCase.assertEqual(test1, 4)

test2 = solution.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])
testCase.assertEqual(test2, 5)

test3 = solution.longestStrChain(["abcd","dbqca"])
testCase.assertEqual(test3, 1)