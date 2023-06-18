from typing import List
import heapq

class Solution:
  def connectSticks(self, sticks: List[int]) -> int:
    heapq.heapify(sticks)
    cost = 0
    
    while sticks.__len__() > 1:
      s1 = heapq.heappop(sticks)
      s2 = heapq.heappop(sticks)
      sum = s1 + s2
      cost += sum
      heapq.heappush(sticks, (s1 + s2))
    
    return cost
  
solution = Solution()
print(solution.connectSticks(
  [1,8,3,5]
))