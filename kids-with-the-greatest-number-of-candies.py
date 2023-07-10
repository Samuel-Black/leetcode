from typing import List
import heapq

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    
    n = len(candies)
    greatest = max(candies)
    # heapq.heapify(maxHeap)
    
    res = [False] * n
    
    for i in range(0, n):
      if candies[i] + extraCandies >= greatest:
        res[i]=True
    return res
    
solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3))