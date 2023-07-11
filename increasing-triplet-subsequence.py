from typing import List

class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    n = len(nums)
    
    left = mid = (2**31) + 1
    
    for i in range(0, n):
      
      if nums[i] < left:
        left = nums[i]
      elif nums[i] < mid:
        if nums[i] <= left:
          left = nums[i]
        else:
          mid = nums[i]
      else:
        if nums[i] <= mid:
          mid = nums[i]
        else:
          return True
      
    return False
        
        
      
    
solution = Solution()
print(solution.increasingTriplet([1,2,3,4,5]))
print(solution.increasingTriplet([2,4,-2,-3]))