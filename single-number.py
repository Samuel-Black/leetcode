from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    res = 0 
    for num in nums:
        res = res ^ num
    return res
    # nums.sort()
    
    # for i in range(0, len(nums), 2):
    #   if i >= (len(nums) - 2):
    #     return nums[i]
    #   if nums[i] != nums[i + 1]:
    #     return nums[i]
      
    