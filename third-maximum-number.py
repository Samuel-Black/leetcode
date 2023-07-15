from typing import List
import heapq

class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    # n = len(nums)
    max = []
    currentMax = pow(-2,31)
    seen = set()
    for num in nums:
      if num not in seen and len(max) < 3:
        heapq.heappush(max, num)
        seen.add(num)
      elif num not in seen and num > max[0]:
        heapq.heapreplace(max, num)
        seen.add(num)
      if num > currentMax:
        currentMax = num
    if len(max) >= 3:
      return max[0]
    
    return currentMax
    

solution = Solution()
print(solution.thirdMax([3,2,1]))
print(solution.thirdMax([2,2,3,1]))
print(solution.thirdMax([1,2]))