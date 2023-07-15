from typing import List

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    n = len(nums)
    left, right = 0, k - 1
    numSum = sum(nums[0:k])
    currAvg = maxAvg = -(2**31) -1
    
    while right < n:
      currAvg = numSum/k
      maxAvg = currAvg if currAvg > maxAvg else maxAvg
      numSum-=nums[left]
      if right + 1 < n:
        numSum+=nums[right+1]
      left+=1
      right+=1
    return maxAvg
  
solution = Solution()
# print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
print(solution.findMaxAverage([-1], 1))