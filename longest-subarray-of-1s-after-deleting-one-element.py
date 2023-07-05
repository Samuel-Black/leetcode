from typing import List

class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    
    left = right = res = 0
    mid = -1
    # hasZero = False
    n = len(nums)
    
    # leftCount = rightCount = 0
    
    while right < n:
      if mid == -1 and nums[right] == 0:
        # deleted = True
        mid = right
      elif mid != -1 and nums[right] == 0:
        # hasZero = True
        left = mid+1
        mid = right
        # deleted = False
        # left
      res = ((right) - (left)) if res < ((right) - (left)) else res
      right+=1
    
    # if mid == -1:
    #   return max(0, res - 1)
    # else:
    return res
    
solution = Solution()
# print(solution.longestSubarray([1,1,0,1]))
# print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))
print(solution.longestSubarray([1,1,1]))