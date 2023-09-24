# from collections import defaultdict
from unittest import TestCase

class Solution(object):
  def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

    # pascalsTriangle = defaultdict(int)

    # pascalsTriangle[(0,0)] = poured
    pascalsTriangle = [[0] * (query_glass+2) for _ in range(0, (query_row+1))]
    pascalsTriangle[0][0] = poured
    for i in range(0, (query_row)):
      for j in range(0, query_glass+1):
        spillOver = (pascalsTriangle[i][j] - 1) / 2.0
        if spillOver > 0:
          pascalsTriangle[i+1][j] += spillOver
          pascalsTriangle[i+1][j+1] += spillOver
    # i = 1
    # j = 0
    # while i <= query_row <= 100:
    #   topLeft=(i-1,j-1)
    #   topRight=(i-1,j)
    #   topLeftSplillOver = max(0, (pascalsTriangle[topLeft] - 1))
    #   topRightSpillOver = max(0, (pascalsTriangle[topRight] - 1))
    #   spillOver = (topLeftSplillOver + topRightSpillOver)/2.0
    #   pascalsTriangle[(i,j)] = spillOver
    #   j+=1
    #   if j > i:
    #     j = 0
    #     i+=1

    return min(pascalsTriangle[query_row][query_glass], 1)

solution = Solution()
testCase = TestCase()

test1 = solution.champagneTower(1, 1, 1)
testCase.assertEqual(test1, 0.00000)

test2 = solution.champagneTower(2, 1, 1)
testCase.assertEqual(test2, 0.50000)

test3 = solution.champagneTower(100000009, 33, 17)
testCase.assertEqual(test3, 1.00000)

test4 = solution.champagneTower(25, 6, 1)
testCase.assertEqual(test4, 0.18750)