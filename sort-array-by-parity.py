from typing import List

class Solution:
  def sortArrayByParity(self, nums: List[int]) -> List[int]:
    n = len(nums)
    
    for i in range(n-1,-1,-1):
      if nums[i] % 2 != 0:
        temp = nums[i]
        del nums[i]
        nums.append(temp)
        
    return nums
    
solution = Solution()
print(solution.sortArrayByParity([3,1,2,4]))