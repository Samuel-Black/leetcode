from unittest import TestCase

class Solution:
  def kthGrammar(self, n: int, k: int) -> int:
        
    res = ['0']*(k+2)
    for i in range(2, (k+2)):
      res[i] = ''
      for c in res[i-1]:
        if c == '0':
          res[i]+='01'
        elif c == '1':
          res[i]+='10'

    return int(res[k])


solution = Solution()
testCase = TestCase()

test1 = solution.kthGrammar(1, 1)
testCase.assertEqual(test1, 0)

test2 = solution.kthGrammar(2, 1)
testCase.assertEqual(test2, 0)

test3 = solution.kthGrammar(2, 2)
testCase.assertEqual(test3, 1)

test4 = solution.kthGrammar(3, 3)
testCase.assertEqual(test4, 10110)