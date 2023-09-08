from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    
    res = []
    col = 1
    
    for i in range(0, numRows):
      res.append([])
      for j in range(0, col):
        prevRow = i-1
        leftCol = 0 if j-1 < 0 or i-1 < 0 else res[prevRow][j-1]
        rightCol = 0 if j >= col-1 or i-1 < 0 else res[prevRow][j]
        val = max(1, leftCol + rightCol)
        res[i].append(val)
      col+=1
    return res
    
    # res = [[] * numRows for i in range(numRows)]
    
    # row = 0
    
    # while row < numRows:
    #   for i in range(0, row + 1):
    #     # if It's not the first two rows, or it's no an edge of the triangle
    #     if row > 1 and (i > 0 and i < row):
    #       res[row].append(res[(row - 1)][i - 1] + res[(row - 1)][i])
    #     else:
    #       res[row].append(1)
    #   row += 1
    # return res
solution = Solution()
print(solution.generate(5))
print(solution.generate(1))