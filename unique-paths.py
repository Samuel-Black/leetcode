from unittest import TestCase


class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    
    
    dp = [[1] * (n) for _ in range(m)]
      
    for col in range(1, m):
      for row in range(1, n):
        dp[col][row] = dp[col-1][row] + dp[col][row-1]
    
    return dp[-1][-1]
    
    # directions = [
    #   (1, 0), # down
    #   (0, 1) # right
    # ]
    
    # # queue = [[0] * (n) for _ in range(m)]
    # queue = [(0, 0)]
    # # seen = set()
    # # seen = set()
    # paths = 0
    
    # while queue:
    #   (row, col) = queue.pop(0)
    #   for (r, c) in directions:
    #     newRow, newCol = row + r, col + c
    #     if newRow == m and newCol == n:
    #       paths+=1
    #     elif newRow <= m and newCol <= n:
    #       queue.append((newRow, newCol))
    #       # seen.add((newRow, newCol))
    
    # return paths
      
solution = Solution()
testCase = TestCase()

test1 = solution.uniquePaths(3, 7)
testCase.assertEqual(test1, 28)

test2 = solution.uniquePaths(3, 2)
testCase.assertEqual(test2, 3)