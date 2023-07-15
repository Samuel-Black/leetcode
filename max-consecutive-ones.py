from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    longestConsecutive = 0
    count = 0
    for num in nums:
      count = count + 1 if num == 1 else 0
      longestConsecutive = count if count > longestConsecutive else longestConsecutive
      
    return longestConsecutive
  
solution = Solution()
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))