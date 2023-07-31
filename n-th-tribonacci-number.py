class Solution:
  def tribonacci(self, n: int) -> int:
    
    if n < 1:
      return 0
    elif n < 3:
      return 1
    
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n+1):
      dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[-1]
    
    
solution = Solution()
print(solution.tribonacci(4))
print(solution.tribonacci(25))