

from functools import cache


class Solution:
  def numSquares(self, n: int) -> int:
    # @cache()
    # def getPerfectSquare(num: int):
    #   return num**num
    queue = [(n, 0)]
    
    perfectSquares = []
    visited = set()
    
    count = 1
    squareRes = 1
    while squareRes <= n:
      squareRes = count**2
      count+=1
      if squareRes <= n:
        perfectSquares.append(squareRes)
    
    queue = [(0, 0)]
    
    while queue:
      (current, count) = queue.pop(0)
      for square in perfectSquares:
        if current+square == n:
          return count + 1
        elif current + square < n and current + square not in visited:
          queue.append((current + square, count + 1))
          visited.add(current + square)
    return - 1
    # for square in perfectSquares:
      
    
    # perfectSquare = 0
    # count = 1
    # while perfectSquare < n:
    #   perfectSquare = count ** count
    #   perfectSquares.add(perfectSquare)
    #   count+=1
    # res = (10**4) + 1
    # level = 0
    # while queue:
    #   level+=1
    #   (num, distance) = queue.pop(0)
    #   for perfectSquare in perfectSquares:
    #     if num - perfectSquare > 0:
    #       queue.append(((num - perfectSquare), distance+1))
    #     elif num - perfectSquare == 0:
    #       return level
          
    # return res
    
    
solution = Solution()
# print(solution.numSquares(12))
# print(solution.numSquares(13))
print(solution.numSquares(1))