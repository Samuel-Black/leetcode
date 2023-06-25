from typing import List

class Solution:
  def probabilityOfHeads(self, prob: List[float], target: int) -> float:
    odds = target / len(prob)
    res = odds
    for num in prob:
      res *= num
      
    return res
solution = Solution()
# print(solution.probabilityOfHeads([0.5,0.5,0.5,0.5,0.5], 0))
print(solution.probabilityOfHeads([1,1,1,1,1,1,1,1,1,1], 9))