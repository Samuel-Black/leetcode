from typing import List
import heapq

# solution entails using a min heap to always have access to the building with the least distance

# greedily use ladders while adding the distance traversed to the min heap
# once we're out of ladders attempt to use the bricks by popping the minimum distance 
# from the min heap and subtracting it from the amount of bricks
# if the amount of bricks <= 0 that means we've used all ladders and bricks 
class Solution:
  def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> List[int]:
    n = len(heights)
    minHeap = []
    
    for i in range(n-1):
      height = heights[i+1] - heights[i]
      
      if height <= 0:
        continue
      
      # if bricks or ladder is required add to min heap
      # this assumes a ladder is used before the next check
      if height > 0:
        heapq.heappush(minHeap, height)
        
      # if the length of the heap is greater than the number of available ladders
      # this means bricks need to be used
      if len(minHeap) > ladders:
        ## pop the shortest distance from the min heap and subtract that value from the number of available brricks
        bricks -= heapq.heappop(minHeap)
      
      # if the number of bricks left is less than 0 break the loop
      # since we can also infer that we're out of ladders
      if bricks < 0:
        return i
    
    # n - 1 == the index of the building
    return n-1
    
solution = Solution()
print(solution.furthestBuilding(
  # [4,12,2,7,3,18,20,3,19],
  # 10,
  # 2
  [14,3,19,3],
  17,
  0
))