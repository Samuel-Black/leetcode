from typing import List
from unittest import TestCase

class Solution:
  def validWordSquare(self, words: List[str]) -> bool:
    n = len(words)
      
    for i in range(0, n):
      row = words[i]
      col = ""
      m = len(words[i])
      for j in range(0, n):
        if i < len(words[j]):
          col+=words[j][i]
      if row != col:
        return False
    return True

solution = Solution()
testCase = TestCase()

test1 = solution.validWordSquare(["abcd","bnrt","crmy","dtye"])
testCase.assertEqual(test1, True)

test2 = solution.validWordSquare(["abcd","bnrt","crm","dt"])
testCase.assertEqual(test2, True)

test3 = solution.validWordSquare(["ball","area","read","lady"])
testCase.assertEqual(test3, False)