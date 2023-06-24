from typing import List
import heapq

class Solution:
  def mostFrequentEven(self, nums: List[int]) -> int:
    frequencyMap = {}
    k = 0
    res = -1
    
    for num in nums:
      if num % 2 == 0:
        if not frequencyMap.get(num):
          frequencyMap[num] = 1
        else:
          frequencyMap[num]+=1
        if frequencyMap[num] > k or (frequencyMap[num] == k and num < res):
          k = frequencyMap[num]
          res = num
    return res
    
solution = Solution()
print(solution.mostFrequentEven([2,2,5,6,4,4,4]))