import sys
from typing import List
import heapq

class Solution:
  def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    # pairs have to be sorted in order
    minDifferences = []
    minDifference = sys.maxsize
    
    arr.sort()
    
    for i in range(0, (len(arr) - 1)):
      distance = int(abs(arr[i+1] - arr[i]))
      if distance < minDifference:
        minDifference = distance
        minDifferences.clear()
        minDifferences.append([arr[i], arr[i+1]])
      elif distance == minDifference:
        minDifferences.append([arr[i], arr[i+1]])
    return minDifferences
    
    # heapq.heapify(arr)
    
    # while len(arr) > 1:
    #   distance1 = heapq.heappop(arr)
    #   distance2 = arr[0]
    #   distance = int(abs(distance2 - distance1))
    #   if distance < minDifference:
    #     minDifference = distance
    #     minDifferences.clear()
    #     minDifferences.append([distance1, distance2])
    #   elif distance == minDifference:
    #     minDifferences.append([distance1, distance2])
    # return minDifferences
        
solution = Solution()
print(solution.minimumAbsDifference([4,2,1,3]))