import unittest

class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    
    t = s + s
    if s in t[1:-1]:
      return True
    return False
    
solution = Solution()
test = unittest.TestCase()

test1 = solution.repeatedSubstringPattern("abab")
test.assertEqual(test1, True)

test2 = solution.repeatedSubstringPattern("aba")
test.assertEqual(test2, False)

test3 = solution.repeatedSubstringPattern("abcabcabcabc")
test.assertEqual(test3, True)

test4 = solution.repeatedSubstringPattern("ababab")
test.assertEqual(test4, True)