from unittest import TestCase

class Solution:
  def isPalindrome(self, s: str) -> bool:
        
    n = len(s)-1
    left, right = 0, n

    while left <= right:
      leftChar = ""
      rightChar = ""
      while left < right and not s[left].isalnum():
        left+=1
      leftChar = "" if left > n else s[left].lower()
      while right > left and not s[right].isalnum():
        right-=1
      rightChar = "" if left > n else s[right].lower()
      if leftChar != rightChar:
        return False
      left+=1
      right-=1
    return True
  
solution = Solution()
testCase = TestCase()

test1 = solution.isPalindrome("A man, a plan, a canal: Panama")
testCase.assertEqual(test1, True)

test2 = solution.isPalindrome("race a car")
testCase.assertEqual(test2, False)

test3 = solution.isPalindrome(" ")
testCase.assertEqual(test3, True)

test3 = solution.isPalindrome("a  a")
testCase.assertEqual(test3, True)