from typing import List

class Solution:
  def validMountainArray(self, arr: List[int]) -> bool:
    n = len(arr)
    # if n < 3:
    #   return False
    
    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
      i+=1
      
    if i == 0 or i == n - 1:
      return False
    
    while i < n - 1 and arr[i] > arr[i + 1]:
      i+=1
      
    return i == n - 1
    # descending: False
    # peak = False
    # for i in range(0, n - 1):
    #   if arr[i] == arr[i + 1]:
    #     return False
      
    #   if i > 0 and peak == False and arr[i] > arr[i + 1]:
    #     peak = True
    #   elif peak == False and arr[i] < arr[i + 1]:
    #     return False
    #   if peak == True and arr[i] < arr[i + 1]:
    #     return False
      
    # return peak
  
solution = Solution()
# print(solution.validMountainArray([0,1,2,3,2,1]))
print(solution.validMountainArray([9,8,7,6,5,4,3,2,1,0]))
# print(solution.validMountainArray([0,1,2,3,4,5,6,7,8,9]))
