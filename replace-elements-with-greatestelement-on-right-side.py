from typing import List

class Solution:
  def replaceElements(self, arr: List[int]) -> List[int]:
    
    n = len(arr)
    currentMax = -1
    for i in range(n-1, -1, -1):
      temp = arr[i]
      arr[i]=currentMax
      currentMax=max(currentMax, temp)
      
    return arr
    # heapArr = [0] * (n - 1)
    # # ignore last element
    # for i in range(0, n - 1):
    #   heapArr[i] = [-x for x in arr[i + 1: n]]
    #   heapq.heapify(heapArr[i])
    
    # for i in range(0, n - 1):
    #   arr[i] = -heapArr[i][0]
    
    # arr[n-1] = -1
    # return arr
solution = Solution()
print(solution.replaceElements([17,18,5,4,6,1]))