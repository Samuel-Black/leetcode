from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums) - 1
    
    for i in range(n, 0, -1):
      num1 = nums[i]
      num2 = nums[i - 1]
      if num1 == num2:
        del nums[i]
        
    return len(nums)
        
solution = Solution()
print(solution.removeDuplicates([1,1,2]))