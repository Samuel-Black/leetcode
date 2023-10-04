from unittest import TestCase

class Solution:
  def balancedString(self, s: str) -> int:
    n = len(s)
    balance = int(n/4)
    charCount = {
      "Q": 0,
      "W": 0,
      "E": 0,
      "R": 0
    }

    left = right = 0
    currentDiff = 0
    for i in range(0, n):
      # if 
      charCount[s[i]]+=1
      currentDiff = charCount[char] - balance
      # if currentDiff 
    # for c in s:
    #   charCount[c]+=1

    totalDiff = 0
    for char in charCount:
      diff = abs(charCount[char] - balance)
      totalDiff += diff
    return int(totalDiff/2)
solution = Solution()
testCase = TestCase()

# test1 = solution.balancedString("QWER")
# testCase.assertEqual(test1, 0)

# test2 = solution.balancedString("QQWE")
# testCase.assertEqual(test2, 1)

# test3 = solution.balancedString("QQQW")
# testCase.assertEqual(test3, 2)

test4 = solution.balancedString("WWEQERQWQWWRWWERQWEQ")
testCase.assertEqual(test4, 4)