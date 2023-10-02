from unittest import TestCase

class Solution:
  def titleToNumber(self, columnTitle: str) -> int:
    res = ord(columnTitle[0])-64
    n = len(columnTitle)
    for i in range(1, n):
      res = (26 * res) + (ord(columnTitle[i])-64)
    # for c in columnTitle:
    #   # prevChar = ord(c)-64
    #   res *= ord(c)-64
    return res

solution = Solution()
testCase = TestCase()

test1 = solution.titleToNumber("A")
testCase.assertEqual(test1, 1)

test1 = solution.titleToNumber("AB")
testCase.assertEqual(test1, 28)

test1 = solution.titleToNumber("ZY")
testCase.assertEqual(test1, 701)