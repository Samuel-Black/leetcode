from functools import cache
from unittest import TestCase


class Solution:
  def minimumBuckets(self, hamsters: str) -> int:
    # for i in range(0, len(hamsters)):

    # n = len(hamsters)
    # @cache  
    # def dp(index: int):
    #   if index-1 > 0:

    #   if index + 1 < n:


    # return dp(0)

    n = len(hamsters)
    dp = [0] * n
    for i in range(0, n):
      if hamsters[i] != ".":
        continue
      left = max(0, (i-1))
      right = min((n-1), (i+1))

      # -1 case
      if hamsters[i] == hamsters[left] == hamsters[right] == "H":
        return -1
      if hamsters[left] == "H" or hamsters[right] == "H":
        dp[i]+=1
      dp[i] 
        
        # dp[i] = max(hamsters[i])

    return dp[-1]


solution = Solution()
testCase = TestCase()

test1 = solution.minimumBuckets("H..H")
testCase.assertEqual(test1, 2)

test2 = solution.minimumBuckets(".H.H.")
testCase.assertEqual(test2, 1)

test3 = solution.minimumBuckets(".HHH.")
testCase.assertEqual(test3, -1)