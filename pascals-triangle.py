from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    res = [[] * numRows for i in range(numRows)]
    
    row = 0
    
    while row < numRows:
      for i in range(0, row + 1):
        # if It's not the first two rows, or it's no an edge of the triangle
        if row > 1 and (i > 0 and i < row):
          res[row].append(res[(row - 1)][i - 1] + res[(row - 1)][i])
        else:
          res[row].append(1)
      row += 1
    return res
solution = Solution()
print(solution.generate(5))