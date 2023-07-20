from typing import List


class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    
    stack = []
    
    for asteroid in asteroids:
      winner = asteroid
      while stack:
        if winner > 0 and stack[-1] > 0 or winner < 0 and stack[-1] < 0 or stack[-1] < 0 and winner > 0:
          break
        elif abs(winner) > abs(stack[-1]):
          stack.pop()
        elif abs(winner) < abs(stack[-1]):
          winner = stack[-1]
          stack.pop()
        elif abs(winner) == abs(stack[-1]):
          stack.pop()
          winner = None
          break
      if winner:
        stack.append(winner)
    return stack
    
solution = Solution()
print(solution.asteroidCollision([5,10,-5]))
print(solution.asteroidCollision([8, -8]))
print(solution.asteroidCollision([10,2,-5]))
print(solution.asteroidCollision([-2,-1,1,2]))

