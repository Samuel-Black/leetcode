from unittest import TestCase

class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
    
    # cba
    # bac
    # bacd
    # badc
    # adcb
    # adbc  

    res = ""
    dict = {}
    distinctCount = 0
    
    for i in range(0, len(s)):
      if s[i] not in dict:
        dict[s[i]] = i
        queue.append(s[i])
      else:
        queue.pop(dict[s[i]])
        dict[s[i]] = i
        queue.append(s[i])

    return ''.join(queue)

solution = Solution()
testCase = TestCase()

test1 = solution.removeDuplicateLetters("bcabc")
testCase.assertEqual(test1, "abc")

test2 = solution.removeDuplicateLetters("cbacdcbc")
testCase.assertEqual(test2, "acdb")