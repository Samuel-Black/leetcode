from unittest import TestCase

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    
    m = len(s)
    n = len(t)
    sIndex = 0
    if m <= 0:
      return True
    for i in range(0, n):
      if s[sIndex] == t[i]:
        sIndex += 1
        if sIndex > (m-1):
            return True
    return False

    # n = len(s)
    # m = len(t)
    # count = 0
    # i = 0
    # while count < n and i < m:
    #   if s[count] == t[i]:
    #     count+=1
    #   i+=1
    # return count == n
    
solution = Solution()
testCase = TestCase()

test1 = solution.isSubsequence("abc", "ahbgdc")
testCase.assertEqual(test1, True)

test2 = solution.isSubsequence("axc", "ahbgdc")
testCase.assertEqual(test2, False)

test3 = solution.isSubsequence("", "ahbgdc")
testCase.assertEqual(test3, True)