from functools import cache
from typing import List
from unittest import TestCase

class Solution:
  def maximumBooks(self, books: List[int]) -> int:
    n = len(books)
    i = (n-1)
    @cache
    def dp(ceiling: int) -> int:
      if i < 0:
        return 0
      
      currMax = 0
      for j in range(ceiling+1, -1, -1):
        currMax = max((dp(j) + j), currMax)
      return currMax
      # res = 0
      # currMax = 0
      # for i in range(shelf, n):
      #   for j in range(books[shelf], -1, -1):
      # need to get the current value + all previous values of books and 
      # currMax = 0
      # for i in range(ceiling, -1, -1):
      #   currMax = max(dp((i-1), ceiling) + i)
      # currMax = min((floor-1), books[shelf])
      # res+=currMax
      
          # currMax += max(dp(shelf, ceiling), dp(shelf, ceiling-1))

          # return j

        # for j in range(0, currBooks):
        #   maxBooks = max(dp(i), maxBooks)
    
    res = 0

    for i in range(0, n):
      res = max(res, dp(books[i]))

    return res

solution = Solution()
testCase = TestCase()

test1 = solution.maximumBooks([8,5,2,7,9])
testCase.assertEqual(test1, 19)

test2 = solution.maximumBooks([7,0,3,4,5])
testCase.assertEqual(test2, 12)

test3 = solution.maximumBooks([8,2,3,7,3,4,0,1,4,3])
testCase.assertEqual(test3, 13)