from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    
    maxWater = 0
    currentWater = 0
    
    n = len(height)
    
    start, end = 0, (n-1)
    
    while start != end:
      currentWater = min(height[start], height[end]) * (end - start)
      maxWater = currentWater if currentWater > maxWater else maxWater
      if height[start] <= height[end]:
        start+=1
      else:
        end-=1
        
    return maxWater
      
    
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))