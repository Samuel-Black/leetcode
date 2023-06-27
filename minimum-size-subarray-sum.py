from typing import List

class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    n = len(nums)
    left, right = 0, 0
    res = n + 1
    sum = 0
    
    for right in range(0, n):
      sum += nums[right]
      
      while sum >= target:
        res = min(res, (right - left) + 1)
        sum -= nums[left]
        left += 1
        
    return res if res != n + 1 else 0
       
solution = Solution()
print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(solution.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))