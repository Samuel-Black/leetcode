from functools import cache
from typing import List, Optional
import heapq
from queue import PriorityQueue
import math
from collections import defaultdict

# class Solution:
#   def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
#     res = []
#     for word in words:
#       string = ""
#       for i in range(0, len(word)):
#         if word[i] == separator:
#           if string != "":
#             res.append(string)
#           string = ""
#           continue
#         string += word[i]
#       if string != "":
#         res.append(string)
        
        
#     return res

# solution = Solution()
# print(solution.splitWordsBySeparator(["one.two.three","four.five","six"], "."))
# print(solution.splitWordsBySeparator(["$easy$","$problem$"], "$"))
# print(solution.splitWordsBySeparator(["|||"], "|"))

class Node:
  def __init__(self, val: int, i: int):
    self.val = val
    self.i = i
    
  def __lt__(self, other):
    if self.val == other.val:
      return self.i < other.i
    else:
      return self.val < other.val

class Solution:
  def maxArrayValue(self, nums: List[int]) -> int:
    
    # for i in range(len(nums)//2, len(nums)):
        
    i = len(nums) - 1

    while i > 0:
      if nums[i-1] <= nums[i]:
        nums[i-1]+=nums[i]
        nums.pop(i)
        i = len(nums) - 1
      else:
        i-=1
    return max(nums)

    # for i in range(len(nums), -1, -1):
      
      
    # while nums:
    #   arrToMerge = nums[len(nums)//2::]
    #   i = 0
    #   if i+1 < len(nums) and nums[i] <= nums[i+1]:
    #     if i > 0 and nums[i-1] + nums[i] > nums[i] + nums[i] + 1:
    #       i+=1
    #       continue
    #     # if nums[i] + nums[i+1] > rightSum and nums[i] + nums[i + 1] < leftSum:
    #     #   i+=1
    #     #   continue
    #     nums[i]+=nums[i+1]
    #     nums.pop(i+1)
    #     performedMerge = True
    #   # else:
    #   leftSum += nums[i]
    #   if i+1 < len(nums):
    #     rightSum -= nums[i+1]
    #   i+=1
    #   if len(nums) == 1:
    #     return nums[0]
    #   if i == len(nums):
    #     if performedMerge == False:
    #       return max(nums)
    #     i = 0
    #     performedMerge = False
    #     leftSum = 0
    #     rightSum = sum(nums[1::])
    
    # n = len(nums)
    
    # # possibleMerges = {}
    
    # possibleMerge = []
    
    # for i in range(0, n):
    #   if i+1 < len(nums) and nums[i] <= nums[i+1]:
    #     # possibleMerges[i] = nums[i] + nums[i+1]
    #     possibleMerge.append(Node(nums[i] + nums[i+1], i))
    
    # heapq.heapify(possibleMerge)
    # i = 0
    
    # while possibleMerge:
    #   smallestPossibleMerge = heapq.heappop(possibleMerge)
      
    #   nums.pop(smallestPossibleMerge.i+1)
    #   nums[smallestPossibleMerge.i]=smallestPossibleMerge.val
      
    #   possibleMerge = []
    
    #   for i in range(0, len(nums)):
    #     if i+1 < len(nums) and nums[i] <= nums[i+1]:
    #       # possibleMerges[i] = nums[i] + nums[i+1]
    #       possibleMerge.append(Node(nums[i] + nums[i+1], i))
      
      
    # # while possibleMerges:
      
    
    # return max(nums)
    
    # queue = []
    # queue
    
    # n = len(nums)
    # i = 0
    
    # performedMerge = False
    # # currentMax = 0
    # leftSum = 0
    # rightSum = sum(nums[1::])
    
    # while nums:
    #   if i+1 < len(nums) and nums[i] <= nums[i+1]:
    #     if i > 0 and nums[i-1] + nums[i] > nums[i] + nums[i] + 1:
    #       i+=1
    #       continue
    #     # if nums[i] + nums[i+1] > rightSum and nums[i] + nums[i + 1] < leftSum:
    #     #   i+=1
    #     #   continue
    #     nums[i]+=nums[i+1]
    #     nums.pop(i+1)
    #     performedMerge = True
    #   # else:
    #   leftSum += nums[i]
    #   if i+1 < len(nums):
    #     rightSum -= nums[i+1]
    #   i+=1
    #   if len(nums) == 1:
    #     return nums[0]
    #   if i == len(nums):
    #     if performedMerge == False:
    #       return max(nums)
    #     i = 0
    #     performedMerge = False
    #     leftSum = 0
    #     rightSum = sum(nums[1::])
    
    # for i in range(0, n):
    #   if nums[i] <= nums[i+1]:
        
    
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
    # # Choose an integer i such that 0 <= i < nums.length - 1 and nums[i] <= nums[i + 1]. 
    # # Replace the element nums[i + 1] with nums[i] + nums[i + 1] and delete the element nums[i] from the array.
    
    # # nums.sort()
    # n = len(nums)
    # maxElem = max(nums)
    # maxElemPosition = binarySearch(maxElem)
    # for i in range(0, n):
      
    
    # maxHeap = [-x for x in nums]
    
    # heapq.heapify(maxHeap)
    
    # while maxHeap:
    #   currentMax = -(heapq.heappop(nums[0]))
      
solution = Solution()
print(solution.maxArrayValue([2,3,7,9,3]))
print(solution.maxArrayValue([5,3,3]))
print(solution.maxArrayValue([34,95,50,12,25,100,21,3,25,16,76,73,93,46,18]))