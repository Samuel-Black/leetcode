from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
      # Initialize seen_once and seen_twice to 0
      seen_once = seen_twice = 0

      # Iterate through nums
      for num in nums:
        # Update using derived equations
        seen_once = (seen_once ^ num) & (~seen_twice)
        seen_twice = (seen_twice ^ num) & (~seen_once)

      # Return integer which appears exactly once
      return seen_once
    
solution = Solution()
print(solution.singleNumber([2,2,3,2]))
print(solution.singleNumber([0,1,0,1,0,1,99]))
print(solution.singleNumber([30000,500,100,30000,100,30000,100]))