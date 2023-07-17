from functools import cache
from typing import List, Optional
import heapq
from queue import PriorityQueue
import math
from collections import defaultdict


# class Solution:
#   def sumOfSquares(self, nums: List[int]) -> int:
#     sum = 0
#     n = len(nums)
#     for i in range(0, n):
#       if n % (i + 1) == 0:
#         sum += (nums[i]*nums[i])
        
        
#     return sum

# solution = Solution()
# print(solution.sumOfSquares([1,2,3,4]))
# print(solution.sumOfSquares([2,7,1,19,18,3]))

class Solution:
  def maximumBeauty(self, nums: List[int], k: int) -> int:
    
    n = len(nums)
    
    left = right = 0
    
    nums.sort()
    
    res = 0
    
    while right < n:
      startRange = (nums[right] - k)
      # endRange = (nums[right] + k)
      if nums[left] < startRange:
        left+=1
      right+=1
      res = max(res, right - left)
      
    return res
    # n = len(nums)
    # # nums.sort()
    # numsCount = defaultdict(int)
    # # outsideRangeCount = defaultdict(int)
    # # insideRangeCount = defaultdict(int)
    # maxOccur = 0
    # maxOccurNum = 0
    
    # i need to know the number of nums that are outside the range, and the number of nums inside the range
    # the result is equal to chose number + (min(k, range - numver of chosen number inside range))
    
    # for i in range(0, n):
    #   # [nums[i] - k, nums[i] + k]
    #   # if the number is outside the range, add it to the second 
    #   startRange = (nums[i] - k)
    #   endRange = (nums[i] + k)
    #   numsCount[nums[i]]+=1
      
    #   key = tuple([startRange, endRange])
      
    #   maxOccur = max(maxOccur, numsCount[nums[i]])
      
      # if startRange <= nums[i] <= endRange:
      #   insideRangeCount[nums[i]] += 1
      # else:
      #   outsideRangeCount[nums[i]] += 1
        
      
        
      # if there's one element inside the range but 2 outside, 
      # get the amount of numbers available inside the current range, minus the count of the chosen number inside that range
      # totalNums = outsideRangeCount[nums[i]] + insideRangeCount[nums[i]]
      # # lowerbound is 0, upperbound is i
      # # range = min(startRange, 0) 
      # # numsInRange + min(startRange, 0) - i
      # r = max(0, min(endRange, i) - max(startRange, 0))
      # numsInRange = max(r - insideRangeCount[nums[i]], 0)
      # # numsInRange = insideRangeCount[nums[i]] - (max(startRange, 0) + i)
      # maxOccur = max(maxOccur, (totalNums + numsInRange))
      # dict[nums[i]]+=1
      # if maxOccur < dict[num]:
      #   maxOccurNum = num
      # maxOccur = max(maxOccur, dict[num])
      
      # totalNums = outsideRangeCount[nums[i]] + insideRangeCount[nums[i]]

      # r = max(0, min(endRange, i) - max(startRange, 0))
      # numsInRange = r - insideRangeCount[nums[i]]
      # maxOccur = max(maxOccur, totalNums + numsInRange)
      
    # del dict[maxOccurNum]
    
    
    
    # return max(maxOccur, 1)
      

    
solution = Solution()
print(solution.maximumBeauty([4,6,1,2], 2))
print(solution.maximumBeauty([1,1,1,1], 10))
print(solution.maximumBeauty([12, 71], 10))
print(solution.maximumBeauty([52, 34], 21))


# class Solution:
#   def minimumIndex(self, nums: List[int]) -> int:
    
#     # s = sum(nums)
#     n = len(nums)
    
#     rightCount = defaultdict(int)
#     leftCount = 0
    
#     for i in range(0, n):
#       rightCount[nums[i]]+=1
      
#     for i in range(0, n):
#       # if 
      
#     return -1
    
# solution = Solution()
# print(solution.minimumIndex([1,2,2,2]))
# print(solution.minimumIndex([2,1,3,1,1,1,7,1,2,1]))
# print(solution.minimumIndex([3,3,3,3,7,2,2]))