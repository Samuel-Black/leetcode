from functools import lru_cache

class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
    n, m = len(text1), len(text2)
    
    # dp i, cointains 
    dp = []
    for i in range(0, (n+1)):
      dp.append([])
      for j in range(0, (m+1)):
        dp[i].append(0)
        
    
    for i in range((n-1), -1, -1):
      for j in range((m-1), -1, -1):
        # print(dp[i - 1][j - 1])
        dp[i][j] = dp[i + 1][j + 1] + 1 if text1[i] == text2[j] else max(dp[i + 1][j], dp[i][j + 1])
    
    return dp[0][0]
    # @lru_cache(2000)
    # def dp():
      
    
solution = Solution()
print(solution.longestCommonSubsequence("abcde", "ace"))
print(solution.longestCommonSubsequence("abc", "abc"))
print(solution.longestCommonSubsequence("abc", "def"))
print(solution.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))