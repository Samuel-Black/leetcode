from collections import defaultdict
from typing import List

class Solution:
  def deleteAndEarn(self, nums: List[int]) -> int:
    
    # nums.sort()
    
    dict = defaultdict(int)
    memo = {}
    # memo = set()
    # res = [0]*(len(nums)+1)
    
    maxNum = 0
    for num in nums:
      dict[num] += num
      maxNum = dict[num] if dict[num] > maxNum else maxNum
      
    # n = len(nums)

      
      
    def dp(index: int) -> int:
      if index == 0:
        return dict[index]
      if index == 1:
        return max(dict[index], dict[index-1])
      if index not in memo:
        # memo[index] = index
        memo[index] = max(dp(index-1), dp(index-2) + dict[index])
      return memo[index]
    
    return dp(maxNum)
      
    # i = 0
    # maxEarn = 0
    # for key in dp:
    #   if (key-1) not in memo:
    #     maxEarn += max()
    #   if key not in memo:
        
    #   # i+=1
    # return maxEarn
    
    
solution = Solution()
print(solution.deleteAndEarn([3,4,2]))
print(solution.deleteAndEarn([2,2,3,3,3,4]))