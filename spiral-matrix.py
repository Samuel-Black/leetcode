from typing import List

class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    n = len(matrix)
    m = len(matrix[0])
    
    res = []
    
    # store upper wall, lower wall, right wall and left wall as variables
    # as you hit walls update the variables
    # if you hit the right wall: topWall += 1
    # if you hit the bottom wall: rightWall -= 1
    # if you hit the left wall: bottom wall -= 1
    # if you hit the top wall: left wall += 1
    
    topWall, leftWall, bottomWall, rightWall = 0, 0, (n - 1), (m - 1)
    
    row, col = 0, 0
    
    # stop conditions are topWall == bottomWall and leftWall == rightWall
    while len(res) < (m*n):
      # go right
      while col <= rightWall and len(res) < (m*n):
        res.append(matrix[row][col])
        col = col + 1
      if col > rightWall:
        col = rightWall
        topWall += 1
        row += 1
      
      # go down
      while row <= bottomWall and len(res) < (m*n):
        res.append(matrix[row][col])
        row = row + 1
      if row > bottomWall:
        row = bottomWall
        rightWall -= 1
        col -= 1
        
      # go left
      while col >= leftWall and len(res) < (m*n):
        res.append(matrix[row][col])
        col = col - 1
      if col < leftWall:
        col = leftWall
        bottomWall -= 1
        row -= 1
        
      # go up
      while row >= topWall and len(res) < (m*n):
        res.append(matrix[row][col])
        row = row - 1
      if row < topWall:
        row = topWall
        leftWall += 1
        col += 1
    return res
  
solution = Solution()
print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))