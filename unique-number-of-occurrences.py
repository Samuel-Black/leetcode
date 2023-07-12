from collections import defaultdict
from typing import List

class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    
    occurrences = defaultdict(int)
    
    for num in arr:
      occurrences[num]+=1
      
    freq = set(occurrences.values())
    # for num in occurrences:
    #   if occurrences[num] in count:
    #     return False
    #   else:
    #     count[occurrences[num]] = 1
      
    return len(occurrences) == len(freq)
    
solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
print(solution.uniqueOccurrences([1,2]))
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))