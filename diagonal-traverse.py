from typing import List


class Solution:
  def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    n = len(mat)
    m = len(mat[0])
    
    res = [0] * (n * m)
    
    row = 0
    col = 0
    topRightDirection = True
    # direction starts by going up,
    # starts at 0, 0 and tries to go to -1, 1 (so up is m-=1 n+=1 and down is m+=1 n-=1)
    for i in range(0, len(res)):
      res[i] = mat[row][col]
      
      # if 
      
      tempRow = row + (-1 if topRightDirection == True else 1)
      tempCol = col + (1 if topRightDirection == True else -1)
      
      # if row or col has hit an edge/corner
      if tempRow < 0 or tempRow == n or tempCol < 0 or tempCol == m:
        if topRightDirection == True:
            row += (col == m - 1)
            col += (col < m - 1)
            topRightDirection = False
        else:
          col += (row == n - 1)
          row += (row < n - 1)
          topRightDirection = True
      # else continue
      else:
        row = tempRow
        col = tempCol
        
      # if topRightDirection == True:
      #   row -= 1
      #   col += 1
      # else:
      #   row += 1
      #   col -= 1
      
      # # case for hitting the top right corner
      # if row < 0 and col > n - 1:
      #   topRightDirection = False
      #   row = 1
      #   col = n - 1
      # # case for hitting the bottom left corner
      # elif col < 0 and row > m - 1:
      #   topRightDirection = True
      #   col = 1
      #   col = m - 1
        
      # # case for row hitting the left side
      # if row < 0:
      #   topRightDirection = False
      #   row = 0
      # elif row > m - 1:
      #   topRightDirection = True
      #   row = m - 1
      # # case for column hitting an edge
      # if col < 0:
      #   col = 0
      #   topRightDirection = True
      # elif col > n - 1:
      #   col = n - 1
      #   topRightDirection = False
      
    return res
    
solution = Solution()
print(solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.findDiagonalOrder([[1,2],[3,4]]))