from typing import List

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    n = len(nums)
    # nums.sort()
    res = set([i for i in range(1, n + 1)])
    
    for num in nums:
      if num in res:
        res.remove(num)
    
    return list(res)
    
solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))