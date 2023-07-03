from math import ceil
from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:

    # rows
    n = len(board)
    # columns
    m = len(board[0])
    
    grids = {}
    rows = {}
    columns = {}
    
    # count = 0
    
    # test rows
    for i in range(0, n):
      # count = ceil((i+1)/3)
      for j in range(0, m):
        if board[i][j] != ".":
          if rows.get(i) == None:
            rows[i] = [0] * 9
          rows[i][int(board[i][j])-1]+=1
          if rows[i][int(board[i][j])-1] > 1:
            return False
          if columns.get(j) == None:
            columns[j] = [0] * 9
          columns[j][int(board[i][j])-1]+=1
          if columns[j][int(board[i][j])-1] > 1:
            return False
          # if max((j/3), (i/3)) + 1 :
          # gridNum = int(round(((max(j, i)/3)+1) * count))
          gridNum = (j // 3) * 3 + i // 3
          # grids[gridNum] = board[i][j]
          if grids.get(gridNum) == None:
            grids[gridNum] = [0] * 9
          grids[gridNum][int(board[i][j])-1] += 1
          if grids[gridNum][int(board[i][j])-1] > 1:
            return False
            # add break condition here to check if current grid has a count > 1
            
        # grids[j] = 
        # row[i] 
      # count //= 3
    # test columns
    return True
    # print("something")
    

solution = Solution()
print(solution.isValidSudoku(
  [["5","3",".",".","7",".",".",".","."]
  ,["6",".",".","1","9","5",".",".","."]
  ,[".","9","8",".",".",".",".","6","."]
  ,["8",".",".",".","6",".",".",".","3"]
  ,["4",".",".","8",".","3",".",".","1"]
  ,["7",".",".",".","2",".",".",".","6"]
  ,[".","6",".",".",".",".","2","8","."]
  ,[".",".",".","4","1","9",".",".","5"]
  ,[".",".",".",".","8",".",".","7","9"]]
))

print(solution.isValidSudoku(
  [[".",".","4",".",".",".","6","3","."]
  ,[".",".",".",".",".",".",".",".","."]
  ,["5",".",".",".",".",".",".","9","."]
  ,[".",".",".","5","6",".",".",".","."]
  ,["4",".","3",".",".",".",".",".","1"]
  ,[".",".",".","7",".",".",".",".","."]
  ,[".",".",".","5",".",".",".",".","."]
  ,[".",".",".",".",".",".",".",".","."]
  ,[".",".",".",".",".",".",".",".","."]]
))
