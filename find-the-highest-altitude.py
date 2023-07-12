from typing import List

class Solution:
  def largestAltitude(self, gain: List[int]) -> int:
    
    res = 0
    currentAlt = 0
    for alt in gain:
      currentAlt+=alt
      res = max(res, currentAlt)
    return res
  
solution = Solution()
# print(solution.largestAltitude([-5,1,5,0,-7]))
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))