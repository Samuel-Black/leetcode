from unittest import TestCase

class Solution(object):
  def decodeAtIndex(self, S, K):
    size = 0
    # Find size = length of decoded string
    for c in S:
      if c.isdigit():
        size *= int(c)
      else:
        size += 1

    for c in reversed(S):
      K %= size
      if K == 0 and c.isalpha():
        return c

      if c.isdigit():
        size /= int(c)
      else:
        size -= 1
              
    # # res = ""
    # i = 0
    # j = 0
    # currStr = ""
    # currDigit = 0

    # stack = s[0]

    # while s != "":
    #   if s[0].isDigit():
    #     currDigit *= 10
    #     currDigit += int(s[0])
    #   else:
    #     if currDigit > 0:
    #       m = len(currStr)
    #       j += m + ((m*(currDigit-1)))
    #       if j >= k:
    #         return currStr[k % m]
    #       else:
    #         currStr = s[i]
    #         currDigit = 0
    #     else:
    #       currStr += s[i]
    #   i+=1

    # return ""

solution = Solution()
testCase = TestCase()

test1 = solution.decodeAtIndex("leet2code3", 10)
testCase.assertEqual(test1, "o")

test2 = solution.decodeAtIndex("ha22", 5)
testCase.assertEqual(test2, "h")

test3 = solution.decodeAtIndex("a2345678999999999999999", 1)
testCase.assertEqual(test3, "a")