from unittest import TestCase

class Solution:
  def myAtoi(self, s: str) -> int:
    
    # readNumber = False
    n = len(s)
    minimum = -(2**31)
    maximum = (2**31)-1
    isPositive = 1
    res = 0
    i = 0
    # not s[i].isnumeric() and s[i] != "+" and s[i] != "-"
    while i < n and s[i] == " ":
      i+=1

    if i < n and s[i] == "-":
      isPositive = -1
      i+=1
    elif i < n and s[i] == "+":
      i+=1

    while i < n and s[i].isnumeric():
      # if s[i].isnumeric():
      res*=10
      res+=int(s[i])
      i+=1

    # for i in range(0, len(s)):
    #   if s[i] == " ":
    #     continue
    #   elif s[i].isnumeric():
    #     res*=10
    #     res+=int(s[i])
    #     readNumber = True
    #   elif readNumber == False and isPositive == 0 and (s[i] == "-" or s[i] == "+"):
    #     isPositive = -1 if s[i] == "-" else 1
    #   else:
    #     break
    
    if isPositive == -1:
      res *= isPositive
    res = max(minimum, min(res, maximum))
    return res
  
solution = Solution()
testCase = TestCase()

test1 = solution.myAtoi("42")
testCase.assertEqual(test1, 42)

test2 = solution.myAtoi("   -42")
testCase.assertEqual(test2, -42)

test3 = solution.myAtoi("4193 with words")
testCase.assertEqual(test3, 4193)

test4 = solution.myAtoi("words and 987")
testCase.assertEqual(test4, 0)

test5 = solution.myAtoi("-91283472332")
testCase.assertEqual(test5, -2147483648)

test6 = solution.myAtoi("00000-42a1234")
testCase.assertEqual(test6, 0)

test7 = solution.myAtoi("+1")
testCase.assertEqual(test7, 1)