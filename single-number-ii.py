from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
      # Initialize seenOnce and seenTwice to 0
      seenOnce = seenTwice = 0

      # Iterate through nums
      for num in nums:
        # Update using derived equations
        seenOnce = (seenOnce ^ num) & (~seenTwice)
        seenTwice = (seenTwice ^ num) & (~seenOnce)

      # Return integer which appears exactly once
      return seenOnce
    
solution = Solution()
print(solution.singleNumber([2,2,3,2]))
print(solution.singleNumber([0,1,0,1,0,1,99]))
print(solution.singleNumber([30000,500,100,30000,100,30000,100]))