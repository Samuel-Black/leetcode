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
    
    # array is a grid, so allowed traversal directions are up, down, left, and right
    directions = [
      [1, 0], # down
      [-1, 0], # up
      [0, 1], # left
      [0, -1] # right
    ]
    
    n = len(rooms)
    m = len(rooms[0])
    
    queue = []
    
    # add all gates to queue
    for i in range(0, n):
      for j in range(0, m):
        if rooms[i][j] == self.gate:
          queue.append([i,j])
          
    while queue:
      # visited = set()
      current = queue.pop(0)
      
      row = current[0]
      col = current[1]
      
      # search one square around the current square in each direction
      # the current square is equal to the last square + 1
      # initially we search 1 square around all gates, but as we traverse we add each allowed square to the queue as well
      # so complexity for this solution is m*n
      for direction in directions:
        rowDirection = row + direction[0]
        colDirection = col + direction[1]
        if rowDirection < 0 or rowDirection >= n or colDirection < 0 or colDirection >= m or rooms[rowDirection][colDirection] != self.inf:
          continue
        rooms[rowDirection][colDirection] = rooms[row][col] + 1
        queue.append([rowDirection, colDirection])
        
    
    
    
solution = Solution()
print(solution.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))