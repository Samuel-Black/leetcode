from typing import List

class Solution:
  def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    sum = 0
    for i in range(0, n, 2):
      sum += nums[i] 
    return sum
solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))