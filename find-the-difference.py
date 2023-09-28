from collections import defaultdict
from unittest import TestCase


class Solution:
  def findTheDifference(self, s: str, t: str) -> str:

    currentDiff = ""
    # the added character will have an odd number of occurences
    # 
    # for c in t:
      

    sCount = defaultdict(int)
    tCount = defaultdict(int)
    for c in s:
      sCount[c]+=1
    for c in t:
      tCount[c]+=1

    for key in tCount:
      if sCount[key] != tCount[key]:
        return key
    

    return currentDiff

solution = Solution()
testCase = TestCase()

test1 = solution.findTheDifference("abcd", "abcde")
testCase.assertEqual(test1, "e")

test2 = solution.findTheDifference("", "y")
testCase.assertEqual(test2, "y")