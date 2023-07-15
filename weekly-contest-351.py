from functools import cache
from typing import List, Optional
import heapq
from math import gcd

# class Solution:
#   def countBeautifulPairs(self, nums: List[int]) -> int:
#     count = 0
    
#     for i in range(0, len(nums)):
#       num1 = int(str(nums[i])[0])
#       for j in range(i + 1, len(nums)):
#         num2 = int(str(nums[j])[-1])
#         if bltin_gcd(num1, num2) == 1:
#           count += 1
#     return count

# solution = Solution()
# # print(solution.countBeautifulPairs([2,5,1,4]))
# print(solution.countBeautifulPairs([31,25,72,79,74]))

# class Solution:
#   def makeTheIntegerZero(self, num1: int, num2: int) -> int:
#     if num1 % 2 != 0 and num2 % 2 != 0:
#       return -1
#     @cache
#     def f(num1, num2):
#       if num1 <= 
    
# solution = Solution()
# # print(solution.countBeautifulPairs([2,5,1,4]))
# print(solution.makeTheIntegerZero(5, 7))

class Solution:
  def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
    onesCount = nums.count(1)
    # zerosCount = nums.count(0)
    if onesCount <= 0:
      return 0
    if onesCount == 1:
      return 1
    oneCount = 0
    # splitCount = 0
    
    goodArrays = 0
    
    zerosArr = [0] * ((onesCount) + 1)
    
    for num in nums:
      if num == 1:
        oneCount += 1
      else:
        zerosArr[oneCount] += 1
        
      # if this is the last one in the array, end the loop since we can't make any more "good" sub arrays
      # if oneCount == onesCount:
      #   break
    
    del zerosArr[0]
    del zerosArr[-1]
    
    for i in range(0, onesCount):
      if i < len(zerosArr) - 1:
        goodArrays += zerosArr[i]
      # if (i + 1) <= len(zerosArr) - 1:
      #   goodArrays += zerosArr[i+1]
      if (i - 1) >= 0:
        goodArrays += zerosArr[i-1]
    
    return int(goodArrays % (pow(10,9) + 7))
    
solution = Solution()
# print(solution.numberOfGoodSubarraySplits([0,1,0]))
# print(solution.numberOfGoodSubarraySplits([0,1,0,0,1]))
print(solution.numberOfGoodSubarraySplits([1,0,0,0,0,0,1,0,1]))


# class Solution:
#   def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
#     res = []
#     n = len(directions)
#     for i in range(0, n):
#       # if directions are not both right or both left there's a collision
#       if directions[i] != directions[i + 1]:
#         newHealth = abs(healths[i] < healths[i + 1])
#         if healths[i] > healths[i + 1]:
#           # update end of res
#           res[-1] = abs(healths[i] < healths[i + 1])
#           # update the values of 
#           res[-1] = abs(healths[i] < healths[i + 1])
          
#         # if they are equal, the robot at the end of res has died and so has the robot at i+1
#         else:
#           del res[-1]
        
#       # if no collision just append
#       else:
#         res.append(healths[i])
    
# solution = Solution()
# print(solution.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL"))