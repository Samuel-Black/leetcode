from typing import List
import heapq

class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    res = []
    heapq.heapify(nums)
    while len(nums) > 0:
      res.append(heapq.heappop(nums))
      
    return res
  
solution = Solution()
print(solution.sortArray([5,1,1,2,0,0]))
    