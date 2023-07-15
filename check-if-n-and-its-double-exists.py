from typing import List

class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    map = set()
    for num in arr:
      if num in map:
        return True
      
      map.add(num * 2)

      if num % 2 == 0:
        map.add(int(num / 2))
      
    return False

solution = Solution()
# print(solution.checkIfExist([3,1,7,11]))
# print(solution.checkIfExist([10,2,5,3]))
# print(solution.checkIfExist([-2,0,10,-19,4,6,-8]))
# print(solution.checkIfExist([0,0]))
# print(solution.checkIfExist([7,1,14,11]))
