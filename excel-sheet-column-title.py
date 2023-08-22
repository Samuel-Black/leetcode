import unittest

class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    
    res = ""
    
    while columnNumber > 0:
      columnNumber -= 1
      res = chr((columnNumber % 26) + 65) + res
      # res += chr((columnNumber % 26) + 64)
      columnNumber//=26
      
    return res

solution = Solution()    
test = unittest.TestCase()

test1 = solution.convertToTitle(1)
test.assertEqual(test1, "A")

test2 = solution.convertToTitle(28)
test.assertEqual(test2, "AB")

test3 = solution.convertToTitle(701)
test.assertEqual(test3, "ZY")