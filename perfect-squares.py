

from functools import cache


class Solution:
  def numSquares(self, n: int) -> int:
    # @cache()
    # def getPerfectSquare(num: int):
    #   return num**num
    queue = [(n, 0)]
    
    perfectSquares = set()
    
    perfectSquare = 0
    count = 1
    while perfectSquare < n:
      perfectSquare = count ** count
      perfectSquares.add(perfectSquare)
      count+=1
    res = (10**4) + 1
    level = 0
    while queue:
      level+=1
      (num, distance) = queue.pop(0)
      for perfectSquare in perfectSquares:
        if num - perfectSquare > 0:
          queue.append(((num - perfectSquare), distance+1))
        elif num - perfectSquare == 0:
          return level
          
    return res
    
    
solution = Solution()
# print(solution.numSquares(12))
print(solution.numSquares(13))