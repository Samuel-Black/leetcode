from typing import List


class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    
    # def dp(i: int):
    #   if i < 0:
    #     return 1
    #   if i not in memo:
    #     memo[i] = min(dp(i-1), dp(i-2)+cost[i])
    # memo = {}
    # return min(dp(len(cost)-1))
    n = len(cost)
    dp = [0]*(n+1)
    dp[n] = 0
    for i in range(2, n+1):
      oneStep = dp[i-1] + cost[i-1]
      twoStep = dp[i-2] + cost[i-2]
      dp[i] = min(oneStep, twoStep)
      # dp[i] = cost[i] + min(dp[i+1], dp[i+2])
      
    return dp[-1]
    # return min(dp[0], dp[1])


solution = Solution()
print(solution.minCostClimbingStairs([10,15,20]))
print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
