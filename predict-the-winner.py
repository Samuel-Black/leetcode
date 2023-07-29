from typing import List

class Solution:
  def PredictTheWinner(self, nums: List[int]) -> bool:
    
    def getDiff(left: int, right: int) -> int:
      if left == right:
        return nums[left]
      else:
        leftScore = nums[left] - getDiff(left + 1, right)
        rightScore = nums[right] - getDiff(left, right - 1)
        return max(leftScore, rightScore)
    
    return getDiff(0, len(nums)-1) >= 0
    # left, right = 0, len(nums)-1
    
    # i = 0
    # scores = [0]*2
    
    # while left <= right:
    #   if nums[left] >= nums[]
    
solution = Solution()
print(solution.PredictTheWinner([1,5,2]))
print(solution.PredictTheWinner([1,5,233,7]))