

from unittest import TestCase

class Solution:
  def countSymmetricIntegers(self, low: int, high: int) -> int:
    
    symmetricCount = 0
    
    for i in range(low, high+1):
      # digitCount = 0
      digits = []
      while i > 0:
        digits.append(i%10)
        i//=10
      n = len(digits)
      if n % 2 != 0:
        continue
      if sum(digits[0: int(n/2)]) == sum(digits[int((n/2))::]):
        symmetricCount+=1
        
    return symmetricCount
      
    
solution = Solution()
testCase = TestCase()

test1 = solution.countSymmetricIntegers(1, 100)
testCase.assertEqual(test1, 9)

test2 = solution.countSymmetricIntegers(1200, 1230)
testCase.assertEqual(test2, 4)