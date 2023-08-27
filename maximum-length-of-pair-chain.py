from typing import List
from unittest import TestCase

class Solution:
  def findLongestChain(self, pairs: List[List[int]]) -> int:
    
    pairs.sort(key=lambda x: x[1])
    
    i = 1
    while i < len(pairs):
      if pairs[i-1][1] >= pairs[i][0]:
        pairs.pop(i)
        continue
      i+=1
      
    return len(pairs)
    

solution = Solution()
test = TestCase()

test1 = solution.findLongestChain([[1,2],[2,3],[3,4]])
test.assertEqual(test1, 2)

test2 = solution.findLongestChain([[1,2],[7,8],[4,5]])
test.assertEqual(test2, 3)

test3 = solution.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]])
test.assertEqual(test3, 4)