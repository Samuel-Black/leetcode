from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
    # def binarySearch(nums: List[int], target: int) -> int:
    #   start, end, index = 0, len(nums) -1, len(nums)
    #   while start <= end:
    #     mid = (start + end) // 2
    #     if nums[mid] >= target:
    #       end = mid - 1
    #       index = mid
    #     else:
    #       start = mid + 1
    #   return index
      
    #   return 0
    index = -1
    left, right = 0, len(matrix)-1
    while left <= right:
      mid = (left + right) // 2
      if target >= matrix[mid][0] and target <= matrix[mid][-1]:
        index = mid
        break
      elif target > matrix[mid][0]:
        left = mid + 1
      elif target < matrix[mid][0]:
        right = mid - 1
        index = mid
      
    if index != -1:
      left, right = 0, len(matrix[0])-1
      while left <= right:
        mid = (left + right) // 2
        if target > matrix[index][mid]:
          left = mid + 1
        elif target < matrix[index][mid]:
          right = mid - 1
        if target == matrix[index][mid]:
          return True
          
    return False

      
solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))