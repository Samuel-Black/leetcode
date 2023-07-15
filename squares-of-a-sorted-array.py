from functools import lru_cache
from typing import List

class Solution:
  def sortedSquares(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    # traverse range backwards from n - 0
    for i in range(n - 1, -1, -1):
      if abs(nums[left]) < abs(nums[right]):
        square = nums[right]
        right -= 1
      else:
        square = nums[left]
        left += 1
      result[i] = square * square
    return result
    # k = 0
    # for k in range(0, len(nums)):
    #   if nums[k] >= 0:
    #     break
      
    # sortedSquares = [0] * len(nums)
    # insertedCount = 0
    
    # negativeIndex = k -1
    # positiveIndex = k
    
    # while (negativeIndex >= 0 and positiveIndex < len(nums)):
    #   negativeSquared = self.squareNum(nums[negativeIndex])
    #   positiveSquared = self.squareNum(nums[positiveIndex])
      
    #   if negativeSquared <= positiveSquared:
    #     sortedSquares[insertedCount] = negativeSquared
    #     negativeIndex -= 1
    #   elif positiveSquared < negativeSquared:
    #     sortedSquares[insertedCount] = positiveSquared
    #     positiveIndex += 1
        
    #   insertedCount += 1
    
    # while (negativeIndex >= 0):
    #   negativeSquared = self.squareNum(nums[negativeIndex])
    #   sortedSquares[insertedCount] = negativeSquared
    #   negativeIndex -= 1
    #   insertedCount += 1
    
    # while (positiveIndex < len(nums)):
    #   positiveSquared = self.squareNum(nums[positiveIndex])
    #   sortedSquares[insertedCount] = positiveSquared
    #   positiveIndex += 1
    #   insertedCount += 1
      
    # return sortedSquares
      

  # define function and use caching since calculations will be repeated
  # @lru_cache(maxsize=None)
  # def squareNum(self, num: int) -> int:
  #   return num * num
    
solution = Solution()
print(solution.sortedSquares([-7,-3,2,3,11]))