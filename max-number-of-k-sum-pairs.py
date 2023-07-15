from collections import defaultdict
from typing import List

class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    start = 0
    end = n - 1
    
    nums.sort()
    
    while start < end:
      numSum = nums[start] + nums[end]
      if numSum == k:
        count+=1
        start+=1
        end-=1
      elif numSum < k:
        start+=1
      elif numSum > k:
        end-=1
        
    return count
      
    # count = 0
    # numsDict = defaultdict(int)
    
    # for num in nums:
    #   numsDict[num]+=1
      
    # for num in nums:
    #   num2 = (k) - (num)
    #   if num == num2:
    #     if numsDict[num2] >= 2:
    #       count+=1
    #       numsDict[num]-=2
    #   else:
    #     if numsDict[num] >= 1 and numsDict[num2] >= 1:
    #       count+=1
    #       numsDict[num]-=1
    #       numsDict[num2]-=1
          
    # return count
    
solution = Solution()
# print(solution.maxOperations([1,2,3,4], 5))
print(solution.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))