from collections import defaultdict
from typing import List

class Solution:
  def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    
    n = len(nums1)
    
    sums = defaultdict(int)
    
    for i in range(0, n):
      for j in range(0, n):
        sums[(nums1[i]) + (nums2[j])]+=1
    
    count = 0
    for i in range(0, n):
      for j in range(0, n):
        count += (sums[-((nums3[i]) + (nums4[j]))])
        # if -((nums3[i]) + (nums4[j])) in sums:
        #   count += (sums[-((nums3[i]) + (nums4[j]))])
    return count
    
    
    
solution = Solution()
print(solution.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))
print(solution.fourSumCount([-1,-1], [-1,1], [-1,1], [1,-1]))