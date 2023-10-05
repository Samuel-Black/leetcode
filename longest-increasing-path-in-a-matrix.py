from functools import cache
from typing import List
from unittest import TestCase

class Solution:
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

    # @cache
    # def dp(row: int, col: int) -> int:

        
    directions = [
      (0, -1), # up
      (0, 1), # down
      (-1, 0), # left
      (1, 0), # right
    ]

    m = len(matrix)
    n = len(matrix[0])

    dp = [[1] * m for _ in range(0, n)]

    maxDistance = 1
    # if 
    for r in range(1, m):
      for c in range(1, n):
        for direction in directions:
          row = r + direction[0]
          col = c + direction[1]
          currMaxDistance = dp[r][c]
          if 0 <= row < m and 0 <= col < n and matrix[row][col] < matrix[r][c]:
            dp[r+direction[0]][c+direction[1]] = dp[r][c] + 1
            currMaxDistance = max(currMaxDistance, dp[r+direction[0]][c+direction[1]])
          dp[r][c] = currMaxDistance
          maxDistance = max(currMaxDistance, maxDistance)

    return maxDistance
    
solution = Solution()
testCase = TestCase()

test1 = solution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
testCase.assertEqual(test1, 4)

test2 = solution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
testCase.assertEqual(test2, 4)

test3 = solution.longestIncreasingPath([[1]])
testCase.assertEqual(test3, 1)

test4 = solution.longestIncreasingPath([[1, 2]])
testCase.assertEqual(test4, 2)