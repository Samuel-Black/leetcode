from typing import List

class Solution:
  def findNumberOfLIS(self, nums: List[int]) -> int:
    
    lastNum = -(10**6 + 1)
    left = 0
    longestSequence = 0
    longestSequenceCount = 0
    
    for i in range(0, len(nums)):
      if nums[i] > lastNum:
        if (i - left) + 1 > longestSequence:
          longestSequence = (i - left) + 1
          longestSequence = max((i - left) + 1, longestSequence)
      else:
        left = i

    
solution = Solution()
print(solution.findNumberOfLIS([1,3,5,4,7]))
print(solution.findNumberOfLIS([2,2,2,2,2]))