from typing import List

class Solution:
  def longestOnes(self, nums: List[int], k: int) -> int:
    
    left = 0
    n = len(nums)
    
    for right in range(0, n):
      # e.g. k -= 1 = 1 if nums[right] == 1
      # so k won't decrease if the current right is 1
      k -= 1 - nums[right]

      # if k is less than 0, we stop "growing" the length of the window and start moving the window to the right
      if k < 0:
        k += 1 - nums[left]
        left+=1
        
    return right - left + 1
    

  
solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(solution.longestOnes([0,0,1,1,1,0,0], 0))
print(solution.longestOnes([1,1,1,1,1], 0))