from collections import defaultdict

class Solution:
  def largestVariance(self, s: str) -> int:
    
    charCount = defaultdict(int)
    
    for c in s:
      charCount[c]+=1
      
    for c in charCount:
      if charCount[c] > 1:
        return 2
      
    return 0
    
solution = Solution()
print(solution.largestVariance("aababbb"))