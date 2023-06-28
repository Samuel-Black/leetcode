from typing import List
import heapq

class Solution:
  def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    n = len(costs)
    
    leftHeap = []
    rightHeap = []
    
    if (candidates * 2) <= n:
      leftHeap.extend(costs[0:candidates])
      del costs[0:candidates]
      
      n = len(costs)
      rightHeap.extend(costs[n - candidates:])
      del costs[n - candidates:]
    else:
      leftHeap.extend(costs)
      costs.clear()
    
    heapq.heapify(leftHeap)
    heapq.heapify(rightHeap)
    sum = 0
    
    for i in range(0, k):
      if not rightHeap or (leftHeap and leftHeap[0] <= rightHeap[0]):
        if len(costs) > 0:
          sum += heapq.heapreplace(leftHeap, costs.pop(0))
        else:
          sum += heapq.heappop(leftHeap)
      else:
        if len(costs) > 0:
          sum += heapq.heapreplace(rightHeap, costs.pop())
        else:
          sum += heapq.heappop(rightHeap)
          
    return sum
  
solution = Solution()
print(solution.totalCost([57,33,26,76,14,67,24,90,72,37,30], 11, 2))
print(solution.totalCost([1,2,4,1], 3, 3))