from typing import List

class Solution:
  def __init__(self):
    self.water = '0'
    self.land = '1'
    
  def numIslands(self, grid: List[List[str]]) -> int:
    
    directions = [
      [1, 0], # down
      [-1, 0], # up
      [0, 1], # right
      [0, -1] # left
    ]
    
    visited = set()
    
    n = len(grid)
    m = len(grid[0])
    
    # row = 0
    # col = 0
    # while row * col < n * m:
    count = 0
    for i in range(0, n):
      for j in range(0, m):
        if grid[i][j] == self.land and tuple([i,j]) not in visited:
          count+=1
          queue = [[i, j]]
          while queue:
            curr = queue.pop(0)
            row = curr[0]
            col = curr[1]
            visited.add(tuple(curr))
            for direction in directions:
              rowDirection = row + direction[0]
              colDirection = col + direction[1]
              if rowDirection < 0 or rowDirection >= n or colDirection < 0 or colDirection >= m or grid[rowDirection][colDirection] == self.water or tuple([rowDirection, colDirection]) in visited:
                continue
              queue.append([rowDirection, colDirection])
      return count
    
    
solution = Solution()
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))