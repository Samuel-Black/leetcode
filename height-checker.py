# 19/06/2023 come back later and solve again, solved in O(n^2) using bubble sort due to tutorial

from typing import List
import copy

class Solution:
  def heightChecker(self, heights: List[int]) -> int:
    originalHeights = copy.deepcopy(heights)
    heightsLength = len(heights) - 1
    
    sortingComplete = False
    while sortingComplete == False:
      swapped = False
      for i in range(heightsLength):
        temp = heights[i]
        if temp > heights[i+1]:
          heights[i] = heights[i+1]
          heights[i+1] = temp
          swapped = True
        if (swapped == False and i == heightsLength - 1):
          sortingComplete = True

    differences = 0
    for index, height in enumerate(originalHeights):
      if heights[index] != height:
        differences+=1
        
    return differences
        
        
    
heights = [1,1,4,2,1,3]
solution = Solution()
print(solution.heightChecker(heights))
