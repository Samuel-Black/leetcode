from typing import List
from unittest import TestCase

class Solution:
  def countBits(self, n: int) -> List[int]:
    
    res = []
    
    for i in range(0, n+1):
      res.append(i.bit_count())
    return res
  
solution = Solution()
test = TestCase()

test1 = solution.countBits(2)
test.assertEqual(test1, [0,1,1])

test2 = solution.countBits(5)
test.assertEqual(test2, [0,1,1,2,1,2])