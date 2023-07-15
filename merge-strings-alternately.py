class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    
    res = ""
    
    n = len(word1)
    m = len(word2)
    
    for i in range(0, n):
      res += word1[i]
      if i < m:
        res += word2[i]
        
    if m > n:
      res += word2[n::]
    return res
    
solution = Solution()
print(solution.mergeAlternately())