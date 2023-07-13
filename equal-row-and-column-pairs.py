from collections import defaultdict
from typing import List

class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    
    rows = []
    rows = defaultdict(int)
    columns = defaultdict(int)
    count = 0
    
    for i in range(0, len(grid)):
      column = []
      for j in range (0, len(grid[i])):
        column.append(grid[j][i])
      columns[tuple(column)]+=1
      # if tuple(grid[i]) in columns:
      count+=columns[tuple(grid[i])]
      # if tuple(column) in rows:
      count+=rows[tuple(column)]
      rows[tuple(grid[i])]+=1
      
    return count
      
        
    
solution = Solution()
print(solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(solution.equalPairs([[13,13],[13,13]]))
print(solution.equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))