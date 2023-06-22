from typing import List

class Solution:
  def duplicateZeros(self, arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    i = 0
    while i < (n - 1):
      if arr[i] == 0:
        arr.insert(i, 0)
        i += 2
        arr.pop()
      else:
        i += 1
    # initialize array with the last element since we skip that iteration in our while loop
    # result = [lastElem] * n
    # indexCount = 0
    # while indexCount < (n -1):
    #   if arr[indexCount] == 0:
    #     result[indexCount] = 0
    #     indexCount += 1
    #     result[indexCount] = 0
    #   else:
    #     result[indexCount] = arr[indexCount]
    #   indexCount += 1
      
    # arr.clear()
    # arr.extend(result)
    # arr = result
        
        
    
# arr = [1,0,2,3,0,4,5,0]
arr = [0,4,1,0,0,8,0,0,3]
solution = Solution()
solution.duplicateZeros(arr)
print(arr)