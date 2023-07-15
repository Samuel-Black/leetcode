from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    n = len(strs)
    strs.sort(key=len)
    longestPrefix = strs[0] if n > 0 else ""
    
    for i in range(1, n):
      str = strs[i]
      for j in range(0, len(longestPrefix)):
        if str[j] != longestPrefix[j]:
          longestPrefix = str[0:j]
          break
        
    
    return longestPrefix
    
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["ab", "a"]))