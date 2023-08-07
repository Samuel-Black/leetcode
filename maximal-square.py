from typing import List

class Solution:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    
    n = len(matrix)
    m = len(matrix[0])
    
    dp = [[0] * (m) for _ in range(n)]
    
    
    
    return dp
    
    
solution = Solution()
print(solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(solution.maximalSquare([["0","1"],["1","0"]]))
print(solution.maximalSquare([["0"]]))