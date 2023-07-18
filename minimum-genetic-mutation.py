from typing import List

class Solution:
  def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
    
    def isValidMutation(s1: str, s2: str) -> bool:
      diff = 0
      for i in range(0, len(s1)):
        diff+=1 if s1[i] != s2[i] else 0
      return diff == 1
    
    # start at the end?
    # for each iteration get the next available paths and add them to the queue
    queue = [(startGene, 0)]
    
    visited = set([startGene])
    
    while queue:
      current, count = queue.pop(0)
      
      for mutation in bank:
        if mutation not in visited and isValidMutation(mutation, current):
          if mutation == endGene:
            return count+1
          queue.append((mutation, count+1))
          visited.add(mutation) 

      
      
    return -1
    
    
solution = Solution()
# print(solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))