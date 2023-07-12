from typing import List

class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    
    n = len(nums)
    rightSum = sum(nums)
    leftSum = 0
    
    for i in range(0, n):
      if i > 0:
        leftSum += nums[i-1]
      rightSum -= nums[i]
      if leftSum == rightSum:
        return i
    
    return -1
    
    # pivot, leftSum, rightSum = -1, 0, sum(nums)
    # for i in range(0, len(nums)):
    #   num = nums[i]
    #   rightSum -= num
    #   if leftSum == rightSum:
    #     pivot = i
    #     break
    #   leftSum += num
    # return pivot
      
    
solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6]))
print(solution.pivotIndex([2,1,-1]))