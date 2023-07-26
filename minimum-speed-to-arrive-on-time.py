from collections import defaultdict
from typing import List
from math import gcd, ceil

class Solution:
  def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
    
    left, right = 1, (10**7)
    minSpeed = -1
    
    
    while left <= right:
      mid = (right + left)//2

      timeTaken = 0
      
      for d in dist:
        timeTaken = ceil(timeTaken) + (d/mid)
      if timeTaken <= hour:
        minSpeed = mid
        right = mid - 1
      else:
        left = mid + 1
        
    return minSpeed

    # n = len(dist)
    # maxSpeed = max(dist)
    
    # # add to queue the current iteration/index, then speed, then current time taken
    # queue = [(0, x, 0) for x in range(1, maxSpeed+1)]

    # while queue:
    #   (i, speed, timeTaken) = queue.pop(0)
    #   timeTaken = ceil(timeTaken) + (dist[i]/speed)
    #   if i+1 == n and timeTaken <= hour:
    #     return speed
    #   elif timeTaken <= hour:
    #     queue.append((i+1, speed, timeTaken))
        
      
    # return -1
    
solution = Solution()
print(solution.minSpeedOnTime([1,3,2], 6))
print(solution.minSpeedOnTime([1,3,2], 2.7))
print(solution.minSpeedOnTime([1,3,2], 1.9))
print(solution.minSpeedOnTime([1,1,100000], 2.01))
print(solution.minSpeedOnTime([5,3,4,6,2,2,7], 10.92))