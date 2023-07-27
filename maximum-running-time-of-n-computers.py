from collections import defaultdict
from typing import List


class Solution:
  def maxRunTime(self, n: int, batteries: List[int]) -> int:

    left, right = 1, sum(batteries) // n
    
    while left < right:
      target = right - (right - left) // 2
        
      extra = 0
      for power in batteries:
        extra += min(power, target)
      
      if extra // n >= target:
        left = target
      else:
        right = target - 1
    
    return left
    
    # if n > len(batteries):
    #   return 0
    
    # max = 0
    
    # buckets = [0]*n
    
    # batteries.sort()
    
    # while batteries:
    #   left, right = 0, len(batteries)-1
    #   while left < right:
    #     mid = (left + right) // 2
    
    # capacities = defaultdict(int)
    
    # for battery in batteries:
    #   capacities[battery]+=1
    
    
    
    # if n > len(batteries):
    #   return 0
    
    # batteries.sort()
    
    # buckets = [0]*n
    
    # i = 0
    # for battery in batteries:
    #   buckets[i%n]+=battery
    #   i+=1
    
    # return min(buckets)
    
    # if n > len(batteries):
    #   return 0
    
    # batterySum = sum(batteries)
    
    # maxMinutes = batterySum//n
    
    # return maxMinutes
    
    # computers = [0]*n
    
    # if n > len(batteries):
    #   return 0
    
    # batteries.sort()
    
    # minutes = 0
    
    # while batteries:
    #   for i in range(0, len(computers)):
    #     if computers[i] <= 0 and batteries:
    #       computers[i] = batteries.pop(0)
    #     elif computers[i] > 0:
    #       computers[i] -= 1
    #     else:
    #       return minutes
    #   minutes+=1
    # return minutes
    
solution = Solution()
print(solution.maxRunTime(2, [3,3,3]))
print(solution.maxRunTime(2, [1,1,1,1]))