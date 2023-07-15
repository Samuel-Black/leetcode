from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    res = [1 for i in range(rowIndex + 1)]
    
    # if rowIndex is even the row will contain an odd number of elements,
    # so check for the inverse. 
    # if rowIndex is an even number, there will be an odd number of elements in that row therefore, isEven is false
    # isEven = (rowIndex % 2) != 0
    for i in range (1, (rowIndex//2+1)):
      res[i] = res[i-1] * (rowIndex - i + 1)//i
      res[rowIndex - i] = res[i]
      # the 0th and the rowIndex-th are always == 1
      # the 1th and second last are always == rowIndex
      # the 2th and third last are == (rowIndex - 1) + 
      # res.append()
      # if i == 0 or i == rowIndex:
      #   res.append(1)
      # elif (i == 1) or i == (rowIndex - 1):
      #   res.append(rowIndex)
      # else:
      #   res.append()
        
    return res
        # 1
        #1 1
       #1 2 1
      #1 3 3 1
     #1 4 6 4 1
   #1 5 10 10 5 1
  #1 6 15 20 15 6 1
 #1 7 21 35 35 21 7 1
#1 8 28 56 70 56 28 8 1
solution = Solution()
print(solution.getRow(4))