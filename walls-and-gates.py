from typing import List

class Solution:
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    INF = (2**31) - 1
    GATE = 0
    
    n = len(rooms[0])
    m = len(rooms)


    
    
    
solution = Solution()
print(solution.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))