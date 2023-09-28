from typing import List

class Solution:
  def sortArrayByParity(self, nums: List[int]) -> List[int]:
    left, right = 0, len(nums)-1

    while left < right:
      if nums[left] % 2 != 0 and nums[right] % 2 == 0:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
      if nums[left] % 2 == 0:
        left+=1
      if nums[right] % 2 != 0:
        right-=1

    return nums
    
solution = Solution()
print(solution.sortArrayByParity([3,1,2,4]))