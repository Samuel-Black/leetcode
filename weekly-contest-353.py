from functools import cache
from typing import List, Optional
import heapq
from queue import PriorityQueue
import math
from collections import defaultdict

# class Solution:
#   def theMaximumAchievableX(self, num: int, t: int) -> int:
        
#     # for i in range(0, t):
    
#     return num + (t*2)
      


# solution = Solution()
# print(solution.theMaximumAchievableX(4, 1))
# print(solution.theMaximumAchievableX(3, 2))



class Solution:
  def maximumJumps(self, nums: List[int], target: int) -> int:
    
    maxJumps = 0
    currentJumps = 0
    
    # jumpsTaken = set()
    jumpDict = defaultdict(list)
    
    
    # def traverse(jumps) -> int:
      
    
    n = len(nums)
    
    for i in range(0, n):
      for j in range(i+1, n):
        if -target <= (nums[j] - nums[i]) <= target:
          jumpDict[i].append(j)
    
    
    possibleJumps = jumpDict.get(0)
    
    for jumps in jumpDict:
      # jumpAvailable = jumps
      #   while jumpAvailable:
    # while possibleJumps:
      # possibleJumps = jumpDict[jumps]
      currentJumps += 1
      if (n-1) in possibleJumps:
        maxJumps = currentJumps
      possibleJumps = possibleJumps.get()
      # for possibleJump in possibleJumps:
      #   if n-1 
      #   print(jumpDict[jumps])
    
    return maxJumps
      
     
solution = Solution()
print(solution.maximumJumps([1,3,6,4,1,2], 2))
print(solution.maximumJumps([1,3,6,4,1,2], 3))
print(solution.maximumJumps([1,3,6,4,1,2], 0))
print(solution.maximumJumps([1,0,2], 1))


# class Solution:
#   def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
      
#       # res = []
#       currentNum = 0
#       currentLength = 0
#       maxLength = 0
      
#       for i in range(0, len(nums1)):
#         if (i + 1) < len(nums1):
#           if nums1[i] == nums1[i+1] or nums1[i] == nums2[i+1]:
#             nextNum = nums1[i]
#           elif nums2[i] == nums1[i+1] or nums2[i] == nums2[i+1]:
#             nextNum = nums2[i]
#           else:
#             nextNum = min(nums1[i], nums2[i])
#         if nextNum < currentNum:
#           nextNum = max(nums1[i], nums2[i])
#         if nextNum >= currentNum:
#           currentLength+=1
#           currentNum = nextNum
#         else:
#           currentLength = 0
#           currentNum = min(nums1[i], nums2[i])
#           currentLength+=1
            
#         maxLength = currentLength if currentLength > maxLength else maxLength
          
        
#       return maxLength
      
# solution = Solution()
# # print(solution.maxNonDecreasingLength([2,3,1], [1,2,1]))
# # print(solution.maxNonDecreasingLength([1,3,2,1], [2,2,3,4]))
# # print(solution.maxNonDecreasingLength([1,1], [2,2]))
# # print(solution.maxNonDecreasingLength([1,3,2,1,3,4,5,6,7,8,9], [2,2,3,1,3,4,5,6,7,8,9]))
# # print(solution.maxNonDecreasingLength([1,8], [10,1]))
# # print(solution.maxNonDecreasingLength([3,8], [15,2]))
# print(solution.maxNonDecreasingLength([11,7,7,9], [19,19,1,7]))