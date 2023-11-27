from unittest import TestCase

class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    
    sStack = []
    tStack = []
    
    for c in s:
      if c == "#" and sStack:
        sStack.pop()
      elif c != "#":
        sStack.append(c)
    
    for c in t:
      if c == "#" and tStack:
        tStack.pop()
      elif c != "#":
        tStack.append(c)
    
    return sStack == tStack
    
solution = Solution()
testCase = TestCase()

test1 = solution.backspaceCompare("ab#c", "ad#c")
testCase.assertTrue(test1)

test2 = solution.backspaceCompare("ab##", "c#d#")
testCase.assertTrue(test2)

test3 = solution.backspaceCompare("a#c", "b")
testCase.assertFalse(test3)

test4 = solution.backspaceCompare("y#fo##f", "y#f#o##f")
testCase.assertTrue(test4)