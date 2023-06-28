from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    res = []
    
    # if rowIndex is even the row will contain an odd number of elements,
    # so check for the inverse. 
    # if rowIndex is an even number, there will be an odd number of elements in that row therefore, isEven is false
    isEven = (rowIndex % 2) != 0
    for i in range (0, (rowIndex + 1)):
      # the 0th and the rowIndex-th are always == 1
      # the 1th and second last are always == rowIndex
      # the 2th and third last are == (rowIndex - 1) + 
      
      
      # 1
      #1 1
     #1 2 1
    #1 3 3 1
   #1 4 6 4 1
 #1 5 10 10 5 1
#1 6 15 20 15 6 1
solution = Solution()
print(solution.getRow(3))