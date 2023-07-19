from typing import List

# class Node():
#   def __init__(self, value, next, prev):
    

class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    
    # directions = 
    visited = set(deadends)
    
    up = {}
    for i in range(0, 10):
      up[str(i)]= str((i+1)%10)
    down = {}
    for i in range(10, 0, -1):
      down[str(i%10)] = str((i-1))
    start = "0000"
    
    queue = [(start, 0)]
    
    if start in visited:
      return -1
    if start == target:
      return 0
    
    while queue:
      currentCombination, distance = queue.pop(0)
      for i in range(0, 4):
        upCombination = currentCombination[0:i] + up[currentCombination[i]] + currentCombination[i+1::]
        if upCombination == target:
          return distance+1
        if upCombination not in visited:
          queue.append((upCombination, distance+1))
          visited.add(upCombination)
        downCombination = currentCombination[0:i] + down[currentCombination[i]] + currentCombination[i+1::]
        if downCombination == target:
          return distance+1
        if downCombination not in visited:
          queue.append((downCombination, distance+1))
          visited.add(downCombination)
    return -1
    
    
    
solution = Solution()
print(solution.openLock(["0201","0101","0102","1212","2002"], "0202"))
print(solution.openLock(["8888"], "0009"))
print(solution.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))