from typing import List
from collections import Counter

class Solution:
  def longestSubsequence(self, arr: List[int], difference: int) -> int:
    
    seen = Counter()
    
    for num in arr:
      seen[num] = seen[num - difference]+1
      
    return max(seen.values())
    
solution = Solution()
print(solution.longestSubsequence())