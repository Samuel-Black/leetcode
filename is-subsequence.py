class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    
    n = len(s)
    m = len(t)
    count = 0
    i = 0
    while count < n and i < m:
      if s[count] == t[i]:
        count+=1
      i+=1
    return count == n

      
    
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))