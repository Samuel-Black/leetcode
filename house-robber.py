from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    
    def dp(index: int) -> int:
      if index == 0:
        return nums[0]
      if index == 1:
        return max(nums[0], nums[1])
      if index not in memo:
        # memo[index] = index
        memo[index] = max(dp(index-1), dp(index-2) + nums[index])
      return memo[index]
    memo = {}
    return dp(len(nums) - 1)
    
solution = Solution()
print(solution.rob([1,2,3,1]))
print(solution.rob([2,7,9,3,1]))