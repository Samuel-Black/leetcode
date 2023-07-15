from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left, right, answer = [0] * n, [0] * n, [0] * n
    
    left[0]=1
    
    for i in range(0, n):
      # L[i - 1] already contains the product of elements to the left of 'i - 1'
      # Simply multiplying it with nums[i - 1] would give the product of all 
      # elements to the left of index 'i'
      left[i] = nums[i - 1] * left[i - 1]
    
    for i in range(0, n):
      leftProduct = []
      nums[i] = 
    
    
    
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))