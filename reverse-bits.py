from unittest import TestCase

class Solution:
  def reverseBits(self, n: int) -> int:
    
    nBinary = format(n,"32b")
    binaryReversed = ""

    for i in range((len(nBinary)-1), -1, -1):
      binaryReversed+=nBinary[i]

    return int(binaryReversed,2)

solution = Solution()
testCase = TestCase()

test1 = solution.reverseBits(43261596)
testCase.assertEqual(test1, 964176192)

test2 = solution.reverseBits(4294967293)
testCase.assertEqual(test2, 3221225471)