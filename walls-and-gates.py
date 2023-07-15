from typing import List

class Solution:
  def __init__(self):
    self.inf = (2**31) - 1
    self.gate = 0
    
  def wallsAndGates(self, rooms: List[List[int]]) -> None:

    # add each gate to the stack
    # from each gate traverse and increment a count for each step
    # traversing can be either left, up, right or down
    # if the current space has a value that != -1 and count < currentValue currentSpace = count

    self.traverse(rooms)
    
  def traverse(self, rooms: List[List[int]]):
    
    directions = [
      [1, 0], # down
      [-1, 0], # up
      [0, 1], # left
      [0, -1] # right
    ]
    
    n = len(rooms)
    m = len(rooms[0])
    
    queue = []
    
    for i in range(0, n):
      for j in range(0, m):
        if rooms[i][j] == self.gate:
          queue.append([i,j])
          
    while queue:
      # visited = set()
      current = queue.pop(0)
      
      row = current[0]
      col = current[1]
      
      for direction in directions:
        rowDirection = row + direction[0]
        colDirection = col + direction[1]
        if rowDirection < 0 or rowDirection >= n or colDirection < 0 or colDirection >= m or rooms[rowDirection][colDirection] != self.inf:
          continue
        rooms[rowDirection][colDirection] = rooms[row][col] + 1
        queue.append([rowDirection][colDirection])
        
    
    
    
solution = Solution()
print(solution.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))