from functools import cache
from typing import List, Optional
import heapq
from queue import PriorityQueue
from math import gcd
import math

# class Solution:
#   def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
    
#     n = len(nums)
#     subArr = []
#     max = 0
    
    
#     for i in range(0, n):
#       if len(subArr) < 1 and nums[i] % 2 == 0 and nums[i] <= threshold:
#         subArr.append(nums[i] % 2)
#       elif len(subArr) >= 1 and nums[i] % 2 != subArr[-1] and nums[i] <= threshold:
#         subArr.append(nums[i] % 2)
#       elif len(subArr) >= 1 and nums[i] % 2 == subArr[-1] and nums[i] <= threshold:
#         if nums[i] % 2 == 0:
#           subArr = [nums[i]%2]
#         else:
#           subArr = []
#       if len(subArr) > max:
#         max = len(subArr)
#       if nums[i] > threshold:
#         subArr = []
        
#     return max
    
        

# solution = Solution()
# print(solution.longestAlternatingSubarray([3,2,5,4], 5))
# print(solution.longestAlternatingSubarray([1,2], 2))
# print(solution.longestAlternatingSubarray([2,3,4,5], 4))
# print(solution.longestAlternatingSubarray([4], 1))
# print(solution.longestAlternatingSubarray([1,10,5], 9))
# print(solution.longestAlternatingSubarray([2, 10, 5], 7))
# print(solution.longestAlternatingSubarray([4, 10, 10], 7))
# print(solution.longestAlternatingSubarray([4, 10, 3], 10))



def getPrimeMap(num):
  notPrimeSet = set()
  primeNums = {}

  for i in range(2, num + 1):
    if i in notPrimeSet:
      continue

    for j in range(i*2, num + 1, i):
      notPrimeSet.add(j)

    primeNums[i] = True

  return primeNums    
  
primeMap = getPrimeMap(10**6)

class Solution:
  def findPrimePairs(self, n: int) -> List[List[int]]:
#     def getPrimeMap(num):
#       notPrimeSet = set()
#       primeNums = {}

#       for i in range(2, n + 1):
#         if i in notPrimeSet:
#           continue

#         for j in range(i*2, n + 1, i):
#           notPrimeSet.add(j)

#         primeNums[i] = True

#       return primeNums
    
    iterations = n // 2
    
    res = []
    
    # primeMap = getPrimeMap(iterations)
    
    # if n % 2 != 0:
    num2 = n - (2)
    if primeMap.get(num2) == True:
      res.append([2, num2])
    
    for i in range(3, iterations + 1, 2):
      if primeMap.get(i) == True:
        num2 = (n) - (i)
        if primeMap.get(num2) == True:
          res.append([i, num2])
    
    return res
    
    
      
solution = Solution()
print(solution.findPrimePairs(10))
print(solution.findPrimePairs(2))
print(solution.findPrimePairs(4))