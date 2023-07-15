from typing import List

class Solution:
  def dominantIndex(self, nums: List[int]) -> int:
    res = -1
    n = len(nums)
    largestNum = -1
    secondLargestNum = -1
    for i in range(0, n):
      if nums[i] > largestNum:
        secondLargestNum = largestNum
        largestNum = nums[i]
        res = i
      elif nums[i] > secondLargestNum: 
        secondLargestNum = nums[i]
    
    if largestNum >= secondLargestNum * 2:
      return res
    
    return -1
    
solution = Solution()
# print(solution.dominantIndex([3,6,1,0]))
# print(solution.dominantIndex([0,0,3,2]))
print(solution.dominantIndex([1,2,3,4]))