# import math
from typing import List
import heapq

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    maxHeap = []
    
    for row in matrix:
      for col in row:
        currentMax = maxHeap[0] if maxHeap.__len__() > 0 else 0
        val = col * -1
        if maxHeap.__len__() < k:
          heapq.heappush(maxHeap, val)
        elif val > currentMax:
          heapq.heapreplace(maxHeap, val)
    
    return maxHeap[0] * -1
    # rowCount = matrix.__len__()
    # k -= 1
    
    # rowNumber = math.floor(k / rowCount)
    # columnNumber = k % rowCount
    
    # return matrix[rowNumber][columnNumber]
    
    
solution = Solution()
print(solution.kthSmallest(
  [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
  5
))